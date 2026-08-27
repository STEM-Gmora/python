import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update .deck-header CSS
    # Current:
    #   .deck-header{
    #     display:flex;
    #     align-items:center;
    #     gap:16px;
    #     padding:16px clamp(25px, 7.5vw, 113px) 12px;
    #     flex:0 0 auto;
    #     max-width:1120px;
    #     margin:0 auto;
    #     width:100%;
    #   }
    
    # We want it to be top-left corner, no max-width, standard padding.
    deck_header_css_replacement = """  .deck-header{
    position: absolute;
    top: 0;
    left: 0;
    display:flex;
    align-items:center;
    padding: 24px 32px;
    z-index: 10;
  }"""
    
    content = re.sub(
        r'\.deck-header\s*\{[^}]*\}',
        deck_header_css_replacement,
        content
    )
    
    # Alternatively, just remove the max-width and margin from it if we don't want absolute.
    # Actually, absolute is fine, but maybe just normal block:
    deck_header_css_alt = """  .deck-header{
    display:flex;
    align-items:center;
    padding: 20px 30px;
    flex:0 0 auto;
    width:100%;
  }"""
    content = re.sub(
        r'\.deck-header\{\s*position: absolute;[^\}]*\}', # fallback if already modified
        deck_header_css_alt,
        content
    )
    content = content.replace(deck_header_css_replacement, deck_header_css_alt)

    # 2. Remove step counter element
    content = re.sub(
        r'<div class="step-counter" id="stepCounter">\d+ / \d+</div>',
        '',
        content
    )
    
    # Remove step-counter css
    content = re.sub(
        r'\.step-counter\s*\{[^}]*\}',
        '',
        content
    )

    # 3. Remove JS for stepCounter
    content = re.sub(
        r"const stepCounter = document\.getElementById\('stepCounter'\);",
        r"",
        content
    )
    content = re.sub(
        r"stepCounter\.textContent = [^;]+;",
        r"",
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
