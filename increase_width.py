import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # Update max-width from 720px to 900px for .code-block, .terminal, and .run-btn-wrap
    
    content = re.sub(
        r'(\.code-block\s*\{[^}]*max-width:)720px;',
        r'\g<1>900px;',
        content
    )
    
    content = re.sub(
        r'(\.terminal\s*\{[^}]*max-width:)720px;',
        r'\g<1>900px;',
        content
    )
    
    content = re.sub(
        r'(\.run-btn-wrap\s*\{[^}]*max-width:)720px;',
        r'\g<1>900px;',
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
