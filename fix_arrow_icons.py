import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # We will use clean feather-style chevron SVGs
    left_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>'
    right_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>'
    
    # Update HTML buttons
    content = re.sub(
        r'(<button id="prevBtn" class="arrow-btn"[^>]*>)←(</button>)',
        f'\\g<1>{left_svg}\\g<2>',
        content
    )
    content = re.sub(
        r'(<button id="nextBtn" class="arrow-btn"[^>]*>)→(</button>)',
        f'\\g<1>{right_svg}\\g<2>',
        content
    )

    # Update JavaScript logic
    content = re.sub(
        r"nextBtn\.innerHTML = isLastStep \? '🎉' : '→';",
        f"nextBtn.innerHTML = isLastStep ? '🎉' : '{right_svg}';",
        content
    )

    # Add display: flex to ensure the SVG centers perfectly within the button
    content = re.sub(
        r'style="background: transparent; border: none; font-size: 24px; cursor: pointer; color: var\(--ink\); padding: 4px;"',
        r'style="background: transparent; border: none; font-size: 24px; cursor: pointer; color: var(--ink); padding: 4px; display: flex; align-items: center; justify-content: center;"',
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
