import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # Replacement string
    new_watermark = '<div class="watermark"><strong style="font-weight: 800;"><span style="color: #ef6a5f;">S</span><span style="color: #f4bf50;">T</span><span style="color: #4285F4;">E</span><span style="color: #61c454;">M</span> <span style="color: black;">Gmora</span></strong></div>'
    
    content = re.sub(
        r'<div class="watermark">STEM Gmora</div>',
        new_watermark,
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
