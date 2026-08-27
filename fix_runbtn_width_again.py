import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # Update max-width from whatever it currently is (probably 1050px or 900px) to 720px for .run-btn-wrap
    content = re.sub(
        r'(\.run-btn-wrap\s*\{[^}]*max-width:\s*)(1050px|900px);',
        r'\g<1>720px;',
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
