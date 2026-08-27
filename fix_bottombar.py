import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # Target replacement for .controls CSS block
    if '.controls{' in content:
        content = re.sub(
            r'(\.controls\s*\{[^}]*)border-top:[^;]+;([^}]*\})',
            r'\1\2',
            content
        )
        content = re.sub(
            r'(\.controls\s*\{[^}]*)max-width:[^;]+;([^}]*\})',
            r'\1\2',
            content
        )
        content = re.sub(
            r'(\.controls\s*\{[^}]*)margin:\s*0\s+auto;([^}]*\})',
            r'\1\2',
            content
        )
        # Standardize the padding to match the top header so it looks like a consistent full-width bar
        content = re.sub(
            r'(\.controls\s*\{[^}]*)padding:[^;]+;([^}]*\})',
            r'\1padding: 14px 30px 22px;\2',
            content
        )

    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

updated = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "index.html":
        if update_file(os.path.join(directory, filename)):
            updated += 1
            
print(f"Updated {updated} files.")
