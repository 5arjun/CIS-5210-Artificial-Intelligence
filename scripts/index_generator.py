#!/usr/bin/env python3
"""
Updates README.md with organized index of all notes
"""

import os
import sys 
import re
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import yaml

def load_config():
    """Load configuration from .notesconfig.yml"""
    with open('.notesconfig.yml', 'r') as f:
        return yaml.safe_load(f)

def parse_note_frontmatter(md_file_path):
    """Extract metadata from markdown frontmatter"""
    with open(md_file_path, 'r') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    frontmatter = parts[1]
    
    # Parse fields
    metadata = {}
    metadata['path'] = str(md_file_path)
    metadata['filename'] = md_file_path.stem
    
    title_match = re.search(r'title:\s*"?([^"\n]+)"?', frontmatter)
    metadata['title'] = title_match.group(1) if title_match else md_file_path.stem
    
    date_match = re.search(r'date:\s*"?([^"\n]+)"?', frontmatter)
    metadata['date'] = date_match.group(1) if date_match else ''
    
    tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
    if tags_match:
        tags_str = tags_match.group(1)
        metadata['tags'] = [tag.strip().strip('"\'') for tag in tags_str.split(',')]
    else:
        metadata['tags'] = []
    
    confidence_match = re.search(r'confidence:\s*([0-9.]+)', frontmatter)
    metadata['confidence'] = float(confidence_match.group(1)) if confidence_match else 1.0
    
    return metadata

def gather_all_notes(notes_folder):
    """Scan notes folder and extract all metadata"""
    notes_path = Path(notes_folder)
    all_notes = []
    
    for md_file in notes_path.rglob('*.md'):
        metadata = parse_note_frontmatter(md_file)
        if metadata:
            all_notes.append(metadata)
    
    return sorted(all_notes, key=lambda x: x['date'], reverse=True)

def generate_chronological_index(notes):
    """Generate chronological table of notes"""
    if not notes:
        return "No notes yet. Start uploading!\n"
    
    # Group by month
    by_month = defaultdict(list)
    for note in notes:
        try:
            date_obj = datetime.fromisoformat(note['date'])
            month_key = date_obj.strftime('%Y-%m')
            by_month[month_key].append(note)
        except:
            by_month['undated'].append(note)
    
    output = []
    for month in sorted(by_month.keys(), reverse=True):
        if month != 'undated':
            output.append(f"\n### {month}\n")
        else:
            output.append(f"\n### Undated\n")
        
        output.append("| Date | Title | Tags | Confidence |")
        output.append("|------|-------|------|------------|")
        
        for note in by_month[month]:
            date_display = note['date'][:10] if len(note['date']) >= 10 else note['date']
            tags_display = ', '.join(f"`{tag}`" for tag in note['tags'][:3])
            confidence_display = f"{note['confidence']:.0%}"
            
            # Get relative path from repo root
            relative_path = note['path']
            # Remove leading ./ if present
            if relative_path.startswith('./'):
                relative_path = relative_path[2:]
            
            output.append(f"| {date_display} | [{note['title']}]({relative_path}) | {tags_display} | {confidence_display} |")
    
    return '\n'.join(output)

def generate_tag_index(notes):
    """Generate tag-based index"""
    tag_map = defaultdict(list)
    
    for note in notes:
        for tag in note['tags']:
            tag_map[tag].append(note)
    
    if not tag_map:
        return "No tags yet.\n"
    
    output = []
    for tag in sorted(tag_map.keys()):
        note_links = [f"[{n['title']}]({n['path'].replace('notes/', '')})" for n in tag_map[tag]]
        output.append(f"- **{tag}**: {', '.join(note_links)}")
    
    return '\n'.join(output)

def update_readme(config, notes):
    """Update or create README.md with index"""
    readme_path = Path('README.md')
    
    # Calculate statistics
    if notes:
        avg_confidence = f"{sum(n['confidence'] for n in notes) / len(notes):.1%}"
        unique_tags = len(set(tag for note in notes for tag in note['tags']))
    else:
        avg_confidence = "N/A"
        unique_tags = 0
    
    # Generate index content
    class_info = f"""# {config['class_name']}
**Course Code**: {config['class_code']}  
**Semester**: {config['semester']}

---

## 📚 Notes Index

This repository contains automated transcriptions of handwritten notes processed through NoteFlow by Arjun.

"""
    
    chronological_index = generate_chronological_index(notes)
    tag_index = generate_tag_index(notes)
    
    statistics = f"""
---

## 📊 Statistics

- **Total Notes**: {len(notes)}
- **Unique Tags**: {unique_tags}
- **Average Confidence**: {avg_confidence}

---

## 🔖 Browse by Tag

{tag_index}

---

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*  
*Generated automatically by [NoteFlow by Arjun](https://github.com/5arjun/noteflow-template)*
"""
    
    new_readme_content = class_info + chronological_index + statistics
    
    # Write README
    with open(readme_path, 'w') as f:
        f.write(new_readme_content)
    
    print(f"✓ README.md updated with {len(notes)} notes", file=sys.stderr)

def main():
    config = load_config()
    notes = gather_all_notes(config['default_notes_folder'])
    update_readme(config, notes)

if __name__ == '__main__':
    main()
