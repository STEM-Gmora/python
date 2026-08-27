import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update .code-block
    if 'flex-shrink: 0;' not in content.split('.code-block {')[1].split('}')[0]:
        content = re.sub(
            r'(\.code-block\s*\{[^}]*)overflow:hidden;',
            r'\g<1>overflow:hidden;\n    display: flex;\n    flex-direction: column;\n    max-height: 50vh;\n    flex-shrink: 0;',
            content
        )
    
    # 2. Update .code-block .header
    content = re.sub(
        r'(\.code-block \.header\s*\{(?![^}]*flex-shrink))',
        r'\1\n    flex-shrink: 0;',
        content
    )
        
    # 3. Update .code-block pre
    content = re.sub(
        r'max-height:none;\s*overflow-x: auto;\s*overflow-y: hidden;',
        r'flex: 1;\n    overflow: auto;',
        content
    )

    # 4. Terminal
    content = re.sub(
        r'(\.terminal\s*\{(?![^}]*flex-shrink))',
        r'\1\n    flex-shrink: 0;\n    display: flex;\n    flex-direction: column;\n    max-height: 50vh;',
        content
    )
    content = re.sub(
        r'(\.terminal-body\s*\{(?![^}]*flex:))',
        r'\1\n    flex: 1;',
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
