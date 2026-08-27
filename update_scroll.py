import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # 1. Update .code-block pre CSS
    # From:
    #   .code-block pre {
    #     ...
    #     overflow-y:auto;
    #     white-space: pre-wrap;
    #   }
    # To:
    #   .code-block pre {
    #     ...
    #     overflow: auto;
    #     white-space: pre;
    #   }
    content = re.sub(
        r'overflow-y:\s*auto;\s*white-space:\s*pre-wrap;',
        r'overflow: auto;\n    white-space: pre;',
        content
    )

    # 2. Update .terminal-body to also have overflow:auto and white-space:pre
    # From:
    #   .terminal-body{
    #     padding:18px 20px 20px;
    #     font-family:'JetBrains Mono',monospace;
    #     font-size:18px;
    #     color:var(--code-ink);
    #     min-height:96px;
    #   }
    # To:
    #   .terminal-body{
    #     padding:18px 20px 20px;
    #     font-family:'JetBrains Mono',monospace;
    #     font-size:18px;
    #     color:var(--code-ink);
    #     min-height:96px;
    #     overflow: auto;
    #     white-space: pre;
    #     max-height: 50vh;
    #   }
    content = re.sub(
        r'(\.terminal-body\{[^}]*min-height:96px;)\s*\}',
        r'\1\n    overflow: auto;\n    white-space: pre;\n    max-height: 50vh;\n  }',
        content
    )

    # 3. Auto-scroll to bottom when appending output
    # From:
    #   codeBlock.querySelector('pre').appendChild(outLine);
    # To:
    #   const preElement = codeBlock.querySelector('pre');
    #   preElement.appendChild(outLine);
    #   preElement.scrollTop = preElement.scrollHeight;
    content = re.sub(
        r"codeBlock\.querySelector\('pre'\)\.appendChild\(outLine\);",
        r"const preElement = codeBlock.querySelector('pre');\n          preElement.appendChild(outLine);\n          preElement.scrollTop = preElement.scrollHeight;",
        content
    )

    # 4. Remove ArrowUp and ArrowDown and Space from slide navigation so scrolling works
    # From:
    #   if (['ArrowRight', 'ArrowDown', ' '].includes(e.key)) { e.preventDefault(); next(); }
    #   if (['ArrowLeft', 'ArrowUp'].includes(e.key)) { e.preventDefault(); prev(); }
    # To:
    #   if (['ArrowRight'].includes(e.key)) { e.preventDefault(); next(); }
    #   if (['ArrowLeft'].includes(e.key)) { e.preventDefault(); prev(); }
    content = re.sub(
        r"if \(\['ArrowRight', 'ArrowDown', ' '\]\.includes\(e\.key\)\) \{ e\.preventDefault\(\); next\(\); \}",
        r"if (['ArrowRight', ' '].includes(e.key)) { e.preventDefault(); next(); }",
        content
    )
    content = re.sub(
        r"if \(\['ArrowLeft', 'ArrowUp'\]\.includes\(e\.key\)\) \{ e\.preventDefault\(\); prev\(\); \}",
        r"if (['ArrowLeft'].includes(e.key)) { e.preventDefault(); prev(); }",
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
