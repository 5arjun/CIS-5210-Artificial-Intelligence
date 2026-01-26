#!/usr/bin/env python3
"""
Processes images using Google Cloud Vision OCR
Groups pages by filename header and orders them
"""

import os
import sys
import json
import re
from pathlib import Path
from google.cloud import vision
from google.oauth2 import service_account
import yaml

def load_config():
    """Load configuration from .notesconfig.yml"""
    with open('.notesconfig.yml', 'r') as f:
        return yaml.safe_load(f)

def load_validation_results():
    """Load results from validation step"""
    with open('/tmp/validation_results.json', 'r') as f:
        return json.load(f)

def extract_header_from_image(client, image_path, top_percent=0.10):
    """OCR just the top portion to extract filename and page number"""
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    # Use DOCUMENT_TEXT_DETECTION for better handwriting recognition
    response = client.document_text_detection(image=image)
    
    if response.error.message:
        raise Exception(f'OCR Error: {response.error.message}')
    
    # Get only the very first line (header line)
    full_text = response.full_text_annotation.text
    lines = full_text.strip().split('\n')
    
    # The header should be the first line only
    if lines:
        header_text = lines[0].strip()
        print(f"    Raw header line: '{header_text}'", file=sys.stderr)
    else:
        header_text = ""
    
    return parse_header_text(header_text)

def parse_header_text(header_text):
    """Parse folder, filename and page number from header text"""
    # Look for patterns like:
    # "SecurityPlus/Vocab words 4/1"
    # "SecurityPlus/vocab-words"
    
    print(f"    Parsing header: {header_text}", file=sys.stderr)
    
    # Clean up the header text
    header_text = header_text.strip()
    
    # Pattern 1: folder/filename page_num/total_pages
    # Pattern 2: folder/filename
    pattern = r'^([a-zA-Z0-9\s\-_+]+)[/|]([a-zA-Z0-9\s\-_]+?)(?:\s+(\d+)/(\d+))?$'
    match = re.search(pattern, header_text, re.IGNORECASE)
    
    if match:
        folder = match.group(1).strip()
        filename = match.group(2).strip()
        
        # Clean folder and filename (replace spaces with hyphens, remove special chars)
        folder = re.sub(r'[^\w\s-]', '', folder)
        folder = re.sub(r'\s+', '-', folder)
        
        filename = re.sub(r'[^\w\s-]', '', filename)
        filename = re.sub(r'\s+', '-', filename)
        
        # Limit filename length
        if len(filename) > 50:
            filename = filename[:50]
        
        # Parse page info
        if match.group(3) and match.group(4):
            current = int(match.group(3))
            total = int(match.group(4))
        else:
            current, total = 1, 1
        
        print(f"    ✓ Parsed: folder='{folder}', filename='{filename}', page={current}/{total}", file=sys.stderr)
            
        return {
            'folder': folder,
            'filename': filename,
            'page_current': current,
            'page_total': total
        }
    else:
        # Try simple pattern without folder (just filename and optional page)
        simple_pattern = r'^([a-zA-Z0-9\s\-_]+?)(?:\s+(\d+)/(\d+))?$'
        simple_match = re.search(simple_pattern, header_text, re.IGNORECASE)
        
        if simple_match:
            filename = simple_match.group(1).strip()
            filename = re.sub(r'[^\w\s-]', '', filename)
            filename = re.sub(r'\s+', '-', filename)
            
            # Limit filename length
            if len(filename) > 50:
                filename = filename[:50]
            
            if simple_match.group(2) and simple_match.group(3):
                current = int(simple_match.group(2))
                total = int(simple_match.group(3))
            else:
                current, total = 1, 1
            
            print(f"    ✓ Parsed (no folder): filename='{filename}', page={current}/{total}", file=sys.stderr)
            
            return {
                'folder': None,
                'filename': filename,
                'page_current': current,
                'page_total': total
            }
        
        # No clear header found, use timestamp-based naming
        print(f"    ⚠ No clear header pattern found", file=sys.stderr)
        return {
            'folder': None,
            'filename': 'untitled',
            'page_current': 1,
            'page_total': 1
        }

def process_full_image_ocr(client, image_path):
    """Perform full OCR on image"""
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    
    if response.error.message:
        raise Exception(f'OCR Error: {response.error.message}')
    
    # Extract text and confidence
    full_text = response.full_text_annotation.text
    
    # Calculate average confidence
    confidences = []
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            confidences.append(block.confidence)
    
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
    
    return {
        'text': full_text,
        'confidence': avg_confidence
    }

def group_and_order_pages(processed_images):
    """Group pages by filename and order by page number and timestamp"""
    groups = {}
    
    for img in processed_images:
        filename = img['header']['filename']
        if filename not in groups:
            groups[filename] = []
        groups[filename].append(img)
    
    # Sort each group by page number, then timestamp
    for filename in groups:
        groups[filename].sort(key=lambda x: (
            x['header']['page_current'],
            x['metadata']['timestamp']
        ))
    
    return groups

def main():
    config = load_config()
    validation_results = load_validation_results()
    
    # Initialize Google Cloud Vision client
    credentials = service_account.Credentials.from_service_account_file(
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    )
    client = vision.ImageAnnotatorClient(credentials=credentials)
    
    processed_images = []
    
    print(f"Processing {validation_results['valid_count']} images...", file=sys.stderr)
    
    for img_metadata in validation_results['images']:
        img_path = os.path.join('notes-inbox', img_metadata['filename'])
        print(f"Processing: {img_metadata['filename']}", file=sys.stderr)
        
        try:
            # Extract header to get filename and page info
            header_info = extract_header_from_image(client, img_path)
            
            # Perform full OCR
            ocr_result = process_full_image_ocr(client, img_path)
            
            processed_images.append({
                'source_file': img_metadata['filename'],
                'metadata': img_metadata,
                'header': header_info,
                'ocr': ocr_result
            })
            
            print(f"  ✓ {header_info['filename']} (page {header_info['page_current']}/{header_info['page_total']}) - Confidence: {ocr_result['confidence']:.2f}", file=sys.stderr)
            
        except Exception as e:
            print(f"  ✗ Error: {str(e)}", file=sys.stderr)
            # Add to failed list but continue
            processed_images.append({
                'source_file': img_metadata['filename'],
                'metadata': img_metadata,
                'header': {'filename': 'failed', 'page_current': 1, 'page_total': 1},
                'ocr': {'text': '', 'confidence': 0.0},
                'error': str(e)
            })
    
    # Group and order pages
    grouped_pages = group_and_order_pages(processed_images)
    
    # Calculate overall statistics
    total_confidence = sum(img['ocr']['confidence'] for img in processed_images if 'error' not in img)
    avg_confidence = total_confidence / len(processed_images) if processed_images else 0.0
    
    output = {
        'grouped_notes': grouped_pages,
        'statistics': {
            'total_images': len(processed_images),
            'unique_notes': len(grouped_pages),
            'average_confidence': avg_confidence
        }
    }
    
    # Save summary files for PR description
    with open('/tmp/avg_confidence.txt', 'w') as f:
        f.write(f"{avg_confidence:.1%}")
    
    # Print JSON to stdout ONLY (no other messages)
    print(json.dumps(output, indent=2))
    
    # Status messages to stderr
    print(f"\n✓ OCR complete! {len(grouped_pages)} unique note files identified", file=sys.stderr)

if __name__ == '__main__':
    main()
