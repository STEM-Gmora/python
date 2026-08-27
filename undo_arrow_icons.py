import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    left_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>'
    right_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>'
    
    # Update HTML buttons back to text characters
    content = content.replace(left_svg, '←')
    content = content.replace(right_svg, '→')

    # Revert display: flex from the button style
    content = re.sub(
        r'style="background: transparent; border: none; font-size: 24px; cursor: pointer; color: var\(--ink\); padding: 4px; display: flex; align-items: center; justify-content: center;"',
        r'style="background: transparent; border: none; font-size: 24px; cursor: pointer; color: var(--ink); padding: 4px;"',
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
