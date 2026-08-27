import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update max-width from 900px to 1050px
    content = re.sub(
        r'(\.code-block\s*\{[^}]*max-width:)900px;',
        r'\g<1>1050px;',
        content
    )
    content = re.sub(
        r'(\.terminal\s*\{[^}]*max-width:)900px;',
        r'\g<1>1050px;',
        content
    )
    content = re.sub(
        r'(\.run-btn-wrap\s*\{[^}]*max-width:)900px;',
        r'\g<1>1050px;',
        content
    )

    # 2. Add width: 100%; to .run-btn and change justify-content to flex-start
    # Currently it has justify-content:center; and no width.
    # Let's replace the whole .run-btn block to be safe.
    new_btn_css = """  .run-btn{
    display:flex;
    align-items:center;
    justify-content:flex-start;
    gap:8px;
    background:#1f2e45;
    color:#fff;
    border:none;
    border-radius:8px;
    padding:10px 16px;
    font-family:'JetBrains Mono',monospace;
    font-size:16px;
    cursor:pointer;
    transition:background .2s ease, transform .1s ease;
    width: 100%;
  }"""
    content = re.sub(r'\.run-btn\s*\{[^}]+\}', new_btn_css, content)

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
