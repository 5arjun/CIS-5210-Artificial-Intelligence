#!/usr/bin/env python3
"""
Formats OCR text into clean Markdown using Perplexity API
Adds tags, cross-references, TODOs, and structure
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
import requests
import yaml

def load_config():
    """Load configuration from .notesconfig.yml"""
    with open('.notesconfig.yml', 'r') as f:
        return yaml.safe_load(f)

def load_ocr_results(input_file):
    """Load OCR results from previous step"""
    with open(input_file, 'r') as f:
        return json.load(f)

def load_existing_notes(notes_folder='notes'):
    """Load existing note files to enable cross-referencing"""
    existing_notes = {}
    notes_path = Path(notes_folder)
    
    if notes_path.exists():
        for md_file in notes_path.rglob('*.md'):
            # Extract title and tags from frontmatter
            with open(md_file, 'r') as f:
                content = f.read()
                # Simple frontmatter parsing
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        title_match = re.search(r'title:\s*"?([^"\n]+)"?', frontmatter)
                        if title_match:
                            existing_notes[md_file.stem] = {
                                'path': str(md_file),
                                'title': title_match.group(1)
                            }
    
    return existing_notes

def call_perplexity_api(prompt, api_key):
    """Call Perplexity API for text formatting"""
    url = "https://api.perplexity.ai/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Use the current valid model name
    # Options: "sonar", "sonar-pro", "sonar-reasoning", "sonar-deep-research"
    # For note formatting, we want fast and cheap, so use basic "sonar"
    payload = {
        "model": "sonar", 
        "messages": [
            {
                "role": "system",
                "content": "You are an expert at formatting handwritten notes into clean, well-structured Markdown with proper academic formatting."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 4000
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as e:
        # Print more detailed error information
        error_detail = ""
        try:
            error_detail = response.json()
        except:
            error_detail = response.text
        print(f"API Error: {e}", file=sys.stderr)
        print(f"Response: {error_detail}", file=sys.stderr)
        raise

def format_with_perplexity(ocr_text, confidence, date, existing_notes, config):
    """Send OCR text to Perplexity for intelligent formatting"""
    
    existing_topics = list(existing_notes.keys())
    topics_context = f"\n\nExisting note topics to cross-reference if relevant: {', '.join(existing_topics)}" if existing_topics else ""
    
    prompt = f"""Convert this OCR text from handwritten notes into clean Markdown format.

CRITICAL: Your response must start with YAML frontmatter between triple dashes, followed by the formatted content.

REQUIREMENTS:
- Start with YAML frontmatter in this EXACT format (no code blocks, no backticks):
---
title: "Descriptive Title Based On Content"
date: {date}
tags: [tag1, tag2, tag3]
confidence: {confidence:.2f}
source: handwritten
---

- After the closing --- of frontmatter, add the formatted content
- Create logical section headers using ## and ###
- Format lists with proper bullets (-) or numbers (1.)
- Preserve mathematical notation using LaTeX: inline as \\( \\) and block as \\[ \\]
- Mark diagrams as [DIAGRAM: description]
- Mark tables as properly formatted Markdown tables if structure is clear
- Extract 3-5 relevant topic tags based on the content
- Highlight questions by making them **bold**
- Extract any TODO items into a dedicated section
- Maintain technical accuracy
- use LaTex for mathematical notation, and ensure it is properly formatted in the output markdown
DO NOT wrap the output in code blocks or backticks. Return raw markdown only.{topics_context}

OCR TEXT (confidence {confidence:.1%}):
{ocr_text}
"""
    
    api_key = os.environ.get('PERPLEXITY_API_KEY')
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable not set")
    
    formatted_text = call_perplexity_api(prompt, api_key)
    
    # Clean up any code block wrappers that Perplexity might add
    formatted_text = formatted_text.strip()
    
    # Remove markdown code blocks if present
    if formatted_text.startswith('```'):
        lines = formatted_text.split('\n')
        # Remove first and last lines if they're code block markers
        if lines.startswith('```'):
            lines = lines[1:]
        if lines and lines[-1].startswith('```'):
            lines = lines[:-1]
        formatted_text = '\n'.join(lines)
    
    # Ensure frontmatter exists, if not add it
    if not formatted_text.startswith('---'):
        print(f"Warning: Perplexity didn't return proper frontmatter, adding it", file=sys.stderr)
        formatted_text = f"""---
title: "Notes from {date}"
date: {date}
tags: []
confidence: {confidence:.2f}
source: handwritten
---

{formatted_text}
"""
    
    return formatted_text

def extract_todos(markdown_text):
    """Extract TODO items from formatted markdown"""
    todos = []
    for line in markdown_text.split('\n'):
        if re.search(r'\[ \]|\[x\]|TODO|todo|To-do', line, re.IGNORECASE):
            todos.append(line.strip())
    return todos

def extract_questions(markdown_text):
    """Extract questions for study review"""
    questions = []
    for line in markdown_text.split('\n'):
        if '?' in line and len(line.strip()) > 5:
            questions.append(line.strip())
    return questions

def extract_tags_from_frontmatter(markdown_text):
    """Extract tags from YAML frontmatter"""
    if markdown_text.startswith('---'):
        parts = markdown_text.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
            if tags_match:
                tags_str = tags_match.group(1)
                return [tag.strip().strip('"\'') for tag in tags_str.split(',')]
    return []

def save_markdown_file(filename, folder, content, config):
    """Save formatted markdown to appropriate folder"""
    notes_folder = Path(config['default_notes_folder'])
    
    # If a specific folder was specified in the header, use it
    if folder:
        target_folder = notes_folder / folder
        target_folder.mkdir(parents=True, exist_ok=True)
    else:
        target_folder = notes_folder
        target_folder.mkdir(exist_ok=True)
    
    output_path = target_folder / f"{filename}.md"
    with open(output_path, 'w') as f:
        f.write(content)
    
    return str(output_path)

def generate_branch_summary(all_tags):
    """Generate a short summary for branch naming"""
    if not all_tags:
        return "notes"  # Default if no tags
    
    # Get most common tags
    from collections import Counter
    tag_counts = Counter(all_tags)
    top_tags = [tag for tag, _ in tag_counts.most_common(3)]
    
    # Clean tags for branch names (remove spaces, special chars)
    clean_tags = [re.sub(r'[^a-zA-Z0-9]+', '-', tag.lower()) for tag in top_tags[:2]]
    
    return '-'.join(clean_tags) if clean_tags else "notes"

def main():
    if len(sys.argv) < 2:
        print("Usage: markdown_formatter.py <ocr_output.json>", file=sys.stderr)
        sys.exit(1)
    
    config = load_config()
    ocr_data = load_ocr_results(sys.argv[1])
    existing_notes = load_existing_notes(config['default_notes_folder'])
    
    all_tags = []
    all_todos = []
    formatted_files = []
    
    print(f"Formatting {len(ocr_data['grouped_notes'])} note documents...", file=sys.stderr)
    
    for note_filename, pages in ocr_data['grouped_notes'].items():
        if note_filename == 'failed':
            print("Skipping failed OCR pages", file=sys.stderr)
            continue
            
        print(f"\nProcessing: {note_filename}", file=sys.stderr)
        
        # Get folder from first page's header
        target_folder = pages[0]['header'].get('folder', None)
        if target_folder:
            print(f"  Target folder: {target_folder}", file=sys.stderr)
        
        # Combine multi-page notes
        combined_text = '\n\n---PAGE BREAK---\n\n'.join(
            page['ocr']['text'] for page in pages if 'error' not in page
        )
        
        avg_confidence = sum(p['ocr']['confidence'] for p in pages if 'error' not in p) / len(pages)
        date = pages[0]['metadata']['timestamp'].split('T')[0]
        
        try:
            # Format with Perplexity
            formatted_md = format_with_perplexity(
                combined_text,
                avg_confidence,
                date,
                existing_notes,
                config
            )
            
            # Extract metadata
            tags = extract_tags_from_frontmatter(formatted_md)
            todos = extract_todos(formatted_md)
            questions = extract_questions(formatted_md)
            
            all_tags.extend(tags)
            all_todos.extend(todos)
            
            # Save file with folder support
            output_path = save_markdown_file(note_filename, target_folder, formatted_md, config)
            formatted_files.append(output_path)
            
            print(f"  ✓ Saved to {output_path}", file=sys.stderr)
            print(f"    Tags: {', '.join(tags)}", file=sys.stderr)
            if todos:
                print(f"    TODOs: {len(todos)}", file=sys.stderr)
            if questions:
                print(f"    Questions: {len(questions)}", file=sys.stderr)
                
        except Exception as e:
            print(f"  ✗ Error formatting {note_filename}: {e}", file=sys.stderr)
    
    # Rest of the function stays the same...

if __name__ == '__main__':
    main()

