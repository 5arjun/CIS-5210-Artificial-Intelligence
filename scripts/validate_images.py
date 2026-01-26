#!/usr/bin/env python3
"""
Validates images in notes-inbox, extracts EXIF data, detects duplicates
"""

import os
import sys
import hashlib
import json
from pathlib import Path
from datetime import datetime
from PIL import Image

# Register HEIF opener for PIL - must be done before opening any HEIF files
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    print("✓ HEIF support enabled", file=sys.stderr)
except ImportError:
    print("⚠ pillow-heif not available, HEIF files may not work", file=sys.stderr)

import yaml

def load_config():
    """Load configuration from .notesconfig.yml"""
    with open('.notesconfig.yml', 'r') as f:
        return yaml.safe_load(f)

def check_image_quality(image_path, min_dpi=200):
    """Check if image meets minimum quality threshold"""
    try:
        # For HEIF files, try to open with pillow_heif first
        if image_path.lower().endswith(('.heic', '.heif')):
            import pillow_heif
            # Read HEIF file and only get the primary image (skip auxiliary images)
            heif_file = pillow_heif.open_heif(image_path, convert_hdr_to_8bit=False)
            
            # Use the primary image only
            img = heif_file.to_pillow()
        else:
            img = Image.open(image_path)
        
        # Get DPI info if available
        dpi = img.info.get('dpi', (0, 0))
        if isinstance(dpi, tuple):
            avg_dpi = sum(dpi) / len(dpi) if len(dpi) > 0 else 0
        else:
            avg_dpi = dpi
            
        # Check resolution as fallback
        width, height = img.size
        min_dimension = min(width, height)
        
        # Be more lenient - most phone photos are good enough
        if min_dimension < 800:
            return False, f"Resolution too low: {width}x{height}"
            
        return True, "OK"
    except Exception as e:
        return False, f"Error reading image: {str(e)}"

def extract_exif_metadata(image_path):
    """Extract EXIF metadata including timestamp"""
    try:
        # For HEIF files, use pillow_heif directly
        if image_path.lower().endswith(('.heic', '.heif')):
            import pillow_heif
            heif_file = pillow_heif.open_heif(image_path, convert_hdr_to_8bit=False)
            img = heif_file.to_pillow()
            
            # Try to get EXIF from the heif metadata
            metadata = {
                'filename': os.path.basename(image_path),
                'size': img.size,
                'format': 'HEIF',
                'timestamp': None,
                'camera': None
            }
            
            # Get EXIF if available
            exif_data = img.getexif() if hasattr(img, 'getexif') else {}
            
        else:
            img = Image.open(image_path)
            exif_data = img.getexif()
            
            metadata = {
                'filename': os.path.basename(image_path),
                'size': img.size,
                'format': img.format,
                'timestamp': None,
                'camera': None
            }
        
        # Extract timestamp (tag 36867 is DateTimeOriginal, 306 is DateTime)
        for timestamp_tag in [36867, 306]:
            if timestamp_tag in exif_data:
                timestamp_str = str(exif_data[timestamp_tag])
                try:
                    metadata['timestamp'] = datetime.strptime(
                        timestamp_str, '%Y:%m:%d %H:%M:%S'
                    ).isoformat()
                    break
                except ValueError:
                    pass
        
        # Fallback to file modification time
        if not metadata['timestamp']:
            mtime = os.path.getmtime(image_path)
            metadata['timestamp'] = datetime.fromtimestamp(mtime).isoformat()
        
        # Extract camera info (tag 272 is Model)
        if 272 in exif_data:
            metadata['camera'] = str(exif_data[272])
            
        return metadata
    except Exception as e:
        print(f"Warning: Could not extract EXIF from {image_path}: {e}", file=sys.stderr)
        # Return basic metadata
        return {
            'filename': os.path.basename(image_path),
            'timestamp': datetime.fromtimestamp(os.path.getmtime(image_path)).isoformat(),
            'size': None,
            'format': None,
            'camera': None
        }

def calculate_file_hash(image_path):
    """Calculate SHA256 hash of image file"""
    sha256_hash = hashlib.sha256()
    with open(image_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def detect_duplicates(image_files):
    """Detect duplicate images by comparing hashes"""
    hashes = {}
    duplicates = []
    
    for img_path in image_files:
        file_hash = calculate_file_hash(img_path)
        if file_hash in hashes:
            duplicates.append({
                'original': hashes[file_hash],
                'duplicate': img_path
            })
        else:
            hashes[file_hash] = img_path
    
    return duplicates

def main():
    config = load_config()
    inbox_path = Path('notes-inbox')
    
    # Get all image files (HEIF, JPG, PNG)
    image_extensions = ['.heic', '.heif', '.jpg', '.jpeg', '.png']
    image_files = [
        str(f) for f in inbox_path.iterdir() 
        if f.suffix.lower() in image_extensions
    ]
    
    if not image_files:
        print("No images found in notes-inbox/", file=sys.stderr)
        sys.exit(0)
    
    print(f"Found {len(image_files)} images to validate", file=sys.stderr)
    
    # Validate quality
    valid_images = []
    invalid_images = []
    
    for img_path in image_files:
        is_valid, message = check_image_quality(
            img_path, 
            config['ocr']['quality_threshold']
        )
        if is_valid:
            valid_images.append(img_path)
        else:
            invalid_images.append({'file': img_path, 'reason': message})
    
    # Detect duplicates
    duplicates = detect_duplicates(valid_images)
    
    # Extract EXIF metadata for valid images
    metadata_list = []
    for img_path in valid_images:
        metadata = extract_exif_metadata(img_path)
        metadata_list.append(metadata)
    
    # Sort by timestamp
    metadata_list.sort(key=lambda x: x['timestamp'])
    
    # Save results
    results = {
        'valid_count': len(valid_images),
        'invalid_count': len(invalid_images),
        'duplicate_count': len(duplicates),
        'images': metadata_list,
        'invalid_images': invalid_images,
        'duplicates': duplicates
    }
    
    with open('/tmp/validation_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✓ Valid images: {len(valid_images)}", file=sys.stderr)
    if invalid_images:
        print(f"✗ Invalid images: {len(invalid_images)}", file=sys.stderr)
        for inv in invalid_images:
            print(f"  - {inv['file']}: {inv['reason']}", file=sys.stderr)
    if duplicates:
        print(f"⚠ Duplicates detected: {len(duplicates)}", file=sys.stderr)
        for dup in duplicates:
            print(f"  - {dup['duplicate']} is duplicate of {dup['original']}", file=sys.stderr)
    
    # Exit with error if all images are invalid
    if len(valid_images) == 0:
        print("ERROR: No valid images to process", file=sys.stderr)
        sys.exit(1)
    
    print("\nValidation complete!", file=sys.stderr)

if __name__ == '__main__':
    main()
