import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Change <a href="index.html" class="home-link"> to <span class="home-link">
    content = content.replace('<a href="index.html" class="home-link">Python Series</a>', '<span class="home-link" style="cursor: default;">Python Series</span>')
    content = content.replace('<a href="index.html" class="home-link">', '<span class="home-link" style="cursor: default;">')
    content = content.replace('</a>\n    <div class="current-topic">', '</span>\n    <div class="current-topic">')
    # Sometimes it might just be the tag end
    content = re.sub(r'(<span class="home-link"[^>]*>.*?)</a>', r'\1</span>', content)

    # 2. Hide the nav-wrapper
    content = content.replace('<div class="nav-wrapper" style="display: flex;', '<div class="nav-wrapper" style="display: none;')
    
    # Also just in case the SVG arrows were reverted and the style string changed:
    # Right now it's:
    # <div class="nav-wrapper" style="display: flex; align-items: center; gap: 14px;">
    
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
