import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update .code-block pre to remove max-height and only allow horizontal scrolling
    if '.code-block pre {' in content:
        content = re.sub(
            r'(\.code-block pre\s*\{[^}]*)max-height:50vh;',
            r'\1max-height:none;',
            content
        )
        content = re.sub(
            r'(\.code-block pre\s*\{[^}]*)overflow: auto;',
            r'\1overflow-x: auto;\n    overflow-y: hidden;',
            content
        )

    # 2. Let's also ensure .slide itself is easily scrollable without getting trapped.
    # It already has overflow-y: auto; which is fine.

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
