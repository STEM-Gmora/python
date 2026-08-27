import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Increase .code-block width to 720px
    content = re.sub(
        r'(\.code-block\s*\{[^}]*max-width:)560px;',
        r'\g<1>720px;',
        content
    )
    
    # 2. Increase .terminal width to 720px
    content = re.sub(
        r'(\.terminal\s*\{[^}]*max-width:)560px;',
        r'\g<1>720px;',
        content
    )

    # 3. Update CSS for .run-btn and add .run-btn-wrap
    if '.run-btn{' in content:
        # replace the whole .run-btn block
        new_css = """  .run-btn{
    display:flex;
    align-items:center;
    justify-content:center;
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
  }
  .run-btn-wrap {
    width: 100%;
    max-width: 720px;
    margin: 8px auto 0;
    display: flex;
    justify-content: flex-end;
  }"""
        
        # We replace the existing .run-btn CSS block entirely
        content = re.sub(r'\.run-btn\s*\{[^}]+\}', new_css, content)

    # 4. Wrap <button class="run-btn...">...</button> in the new wrapper
    # careful not to wrap it multiple times if run multiple times
    if 'class="run-btn-wrap' not in content:
        content = re.sub(
            r'<button class="run-btn([^"]*)">([^<]+)</button>',
            r'<div class="run-btn-wrap\1"><button class="run-btn">\2</button></div>',
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
