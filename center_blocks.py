import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update .code-block CSS
    # Add margin-left: auto; margin-right: auto; if not present
    if '.code-block {' in content:
        content = re.sub(
            r'(\.code-block\s*\{[^}]*margin-top:22px;)',
            r'\1\n    margin-left: auto;\n    margin-right: auto;',
            content
        )

    # 2. Update .terminal CSS
    if '.terminal{' in content:
        content = re.sub(
            r'(\.terminal\s*\{[^}]*margin-top:22px;)',
            r'\1\n    margin-left: auto;\n    margin-right: auto;',
            content
        )

    # 3. Update .run-btn CSS
    if '.run-btn{' in content:
        content = re.sub(
            r'(\.run-btn\s*\{[^}]*margin-top:8px;)',
            r'\1\n    margin-left: auto;\n    margin-right: auto;',
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
