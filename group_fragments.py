import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Remove .fragment from .run-btn-wrap
    content = content.replace('class="run-btn-wrap fragment"', 'class="run-btn-wrap"')

    # 2. Add CSS to link visibility of .run-btn-wrap to the preceding .code-block.fragment
    css_addition = """
  /* Tie run button visibility to its preceding code block if the code block is a fragment */
  .code-block.fragment:not(.visible) + .run-btn-wrap {
    opacity: 0;
    pointer-events: none;
    transform: translateY(10px);
  }
  .code-block.fragment.visible + .run-btn-wrap {
    opacity: 1;
    pointer-events: auto;
    transform: translateY(0);
    transition: opacity .5s var(--ease), transform .5s var(--ease);
  }
"""
    if '.code-block.fragment:not(.visible) + .run-btn-wrap' not in content:
        content = content.replace('</style>', css_addition + '</style>')

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
