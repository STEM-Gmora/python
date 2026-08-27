import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # We want to replace the watermark div and its SVG contents with the old text-based watermark
    # The SVG spans multiple lines, so we use DOTALL to capture everything inside the div
    old_watermark_pattern = r'<div class="watermark"[^>]*>.*?</div>'
    new_watermark = '<div class="watermark" style="text-align: right;"><strong style="font-weight: 800;"><span style="color: #ef6a5f;">S</span><span style="color: #f4bf50;">T</span><span style="color: #4285F4;">E</span><span style="color: #61c454;">M</span> <span style="color: black;">Gmora</span></strong></div>'
    
    content = re.sub(old_watermark_pattern, new_watermark, content, flags=re.DOTALL)

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
