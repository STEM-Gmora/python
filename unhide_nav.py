import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # Restore the display: flex for the nav-wrapper
    content = content.replace('<div class="nav-wrapper" style="display: none; align-items: center; gap: 14px;">', '<div class="nav-wrapper" style="display: flex; align-items: center; gap: 14px;">')
    
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
