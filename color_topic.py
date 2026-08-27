import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # We want to find: &middot; </span>Lesson 09 - Casting</div>
    # And replace with: &middot; </span><span style="color: var(--gold);">Lesson 09 - Casting</span></div>
    
    # We should match: `&middot; </span>` followed by any text that is NOT `<` up to `</div>`
    # However, if it's already wrapped in a span, we should be careful.
    
    # First, let's undo any existing span if present just in case (though we haven't added it yet).
    # content = re.sub(r'<span style="color: var\(--gold\);">([^<]+)</span></div>', r'\1</div>', content)
    
    content = re.sub(
        r'(&middot;\s*</span>)([^<]+)</div>',
        r'\1<span style="color: var(--gold);">\2</span></div>',
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
