#!/bin/bash
# upload-notes.sh - Convert HEIC to JPG and upload notes to GitHub

echo "📸 NoteFlow Upload Script"
echo "========================="
echo ""

# Check if notes-inbox directory exists
if [ ! -d "notes-inbox" ]; then
  echo "❌ notes-inbox/ directory not found"
  echo "💡 Make sure you're in the repo root directory"
  exit 1
fi

# Count HEIC files (more compatible method)
heic_count=0
for ext in HEIC heic; do
  heic_count=$((heic_count + $(ls -1 notes-inbox/*.$ext 2>/dev/null | wc -l)))
done

if [ "$heic_count" -gt 0 ]; then
  echo "🔄 Found $heic_count HEIC file(s) to convert..."
  
  # Convert HEIC to JPG using macOS built-in tool
  for file in notes-inbox/*.HEIC notes-inbox/*.heic; do
    [ -f "$file" ] || continue
    
    filename=$(basename "$file")
    filename_no_ext="${filename%.*}"
    output_file="notes-inbox/${filename_no_ext}.jpg"
    
    echo "   Converting: $filename → ${filename_no_ext}.jpg"
    sips -s format jpeg "$file" --out "$output_file" > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
      # Delete original HEIC after successful conversion
      rm "$file"
      echo "   ✓ Converted and removed original"
    else
      echo "   ⚠️  Conversion failed, keeping original"
    fi
  done
  echo ""
fi

# Check if there are any images to upload
total_count=0
for ext in jpg jpeg JPG JPEG png PNG; do
  total_count=$((total_count + $(ls -1 notes-inbox/*.$ext 2>/dev/null | wc -l)))
done

if [ "$total_count" -eq 0 ]; then
  echo "❌ No images found in notes-inbox/"
  echo "💡 Add your note photos to notes-inbox/ first"
  exit 1
fi

echo "✅ Found $total_count image(s) ready to upload"
echo ""

# Show what will be uploaded
echo "📋 Files to upload:"
for file in notes-inbox/*.jpg notes-inbox/*.jpeg notes-inbox/*.JPG notes-inbox/*.JPEG notes-inbox/*.png notes-inbox/*.PNG; do
  [ -f "$file" ] || continue
  echo "   - $(basename "$file")"
done
echo ""

# Confirm before uploading
read -p "🤔 Upload these notes? (y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "❌ Upload cancelled"
  exit 0
fi

echo "📤 Uploading to GitHub..."
echo ""

# Add, commit, and push
git add notes-inbox/
git commit -m "📝 Add notes from $(date +'%B %d, %Y')"

if [ $? -ne 0 ]; then
  echo "❌ Git commit failed (maybe no changes?)"
  exit 1
fi

git push

if [ $? -eq 0 ]; then
  echo ""
  echo "🎉 Notes uploaded successfully!"
  echo "⏳ GitHub Actions will process your notes in ~2 minutes"
  echo ""
  
  # Get repo URL
  repo_url=$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/' | sed 's/.*github.com[:/]\(.*\)/\1/')
  
  echo "📊 Check progress:"
  echo "   Actions: https://github.com/$repo_url/actions"
  echo "   Pull Requests: https://github.com/$repo_url/pulls"
  echo ""
  echo "💡 Tip: You'll receive a PR with formatted markdown in ~1-2 minutes!"
else
  echo "❌ Git push failed"
  echo "💡 Check your internet connection and GitHub access"
  exit 1
fi
