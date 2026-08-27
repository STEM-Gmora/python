import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # Add width: 100%; to .code-block if it's missing
    content = re.sub(
        r'(\.code-block\s*\{[^}]*margin-left: auto;\n\s*margin-right: auto;\n\s*max-width:1050px;)',
        r'\1\n    width: 100%;',
        content
    )
    
    # Add width: 100%; to .terminal if it's missing
    content = re.sub(
        r'(\.terminal\s*\{[^}]*margin-left: auto;\n\s*margin-right: auto;\n\s*max-width:1050px;)',
        r'\1\n    width: 100%;',
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
