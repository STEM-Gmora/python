import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original_content = content
    
    # The SVG logo replacement
    svg_logo = """<div class="watermark" style="text-align: right; display: flex; align-items: center; justify-content: flex-end; flex: 1;">
      <svg viewBox="0 0 320 120" height="26" xmlns="http://www.w3.org/2000/svg">
        <g font-family="'Arial Black', Impact, sans-serif" font-weight="900" text-anchor="middle">
          <text x="160" y="48" font-size="52" letter-spacing="4">
            <tspan fill="#EA4335">S</tspan><tspan fill="#FBBC04">T</tspan><tspan fill="#4285F4">E</tspan><tspan fill="#34A853">M</tspan>
          </text>
          <text x="160" y="110" font-size="72" letter-spacing="-2" fill="var(--ink, #111)">GMORA</text>
        </g>
      </svg>
    </div>"""

    # We need to find the current watermark div and replace it.
    # Currently it looks like:
    # <div class="watermark" style="text-align: right;"><strong style="font-weight: 800;"><span style="color: #ef6a5f;">S</span><span style="color: #f4bf50;">T</span><span style="color: #4285F4;">E</span><span style="color: #61c454;">M</span> <span style="color: black;">Gmora</span></strong></div>
    
    content = re.sub(
        r'<div class="watermark"[^>]*>.*?</div>',
        svg_logo,
        content,
        flags=re.DOTALL
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
