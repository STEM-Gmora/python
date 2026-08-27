import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update brand in header
    # From: <div class="brand"><span class="dot"></span><span class="hide-mobile">Python Series &middot; </span>
    # To:   <div class="brand"><span class="dot"></span><span class="hide-mobile"><a href="index.html" style="color: inherit; text-decoration: none;">Python Series</a> &middot; </span>
    content = re.sub(
        r'<span class="hide-mobile">Python Series\s*&middot;\s*</span>',
        r'<span class="hide-mobile"><a href="index.html" style="color: inherit; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg> Python Series</a> &middot; </span>',
        content
    )
    # Actually user just said: link index.html to "Python Series" text at the top topic. 
    # Maybe simpler:
    # content = re.sub(
    #     r'<span class="hide-mobile">Python Series &middot; </span>',
    #     r'<span class="hide-mobile"><a href="index.html" style="color: inherit; text-decoration: none;">Python Series</a> &middot; </span>',
    #     content
    # )

    # 2. Remove progress bar track
    content = re.sub(
        r'<div class="progress-track">\s*<div class="progress-fill" id="progressFill"></div>\s*</div>',
        '',
        content
    )

    # 3. Update bottom bar
    # Remove Home button
    content = re.sub(
        r'<a href="index.html" class="btn">.*?Home\s*</a>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Update prev button text
    content = re.sub(
        r'<button id="prevBtn">← Prev</button>',
        r'<button id="prevBtn">←</button>',
        content
    )
    
    # Update next button text
    content = re.sub(
        r'<button id="nextBtn" class="primary">Next →</button>',
        r'<button id="nextBtn" class="primary">→</button>',
        content
    )

    # 4. Update JS for progressFill so it doesn't crash
    content = re.sub(
        r"const progressFill = document\.getElementById\('progressFill'\);",
        r"",
        content
    )
    content = re.sub(
        r"progressFill\.style\.width = progress \+ '%';",
        r"",
        content
    )
    
    # 5. Update JS for nextBtn textContent
    content = re.sub(
        r"nextBtn\.textContent = isLastStep \? '🎉 End of lesson' : 'Next →';",
        r"nextBtn.innerHTML = isLastStep ? '🎉' : '→';",
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
