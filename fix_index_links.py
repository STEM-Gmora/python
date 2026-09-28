import os
import re

directory = "/Users/thanojbuddhima/Development/python-lessons"

# Step 1: Read all actual HTML files to get their real titles/topics
actual_files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'index.html']
actual_files.sort()

file_topics = {}
for f in actual_files:
    with open(os.path.join(directory, f), 'r') as file:
        content = file.read()
        match = re.search(r'<div class="current-topic">([^<]+)</div>', content)
        if match:
            topic = match.group(1)
            # Normalize topic name
            normalized_topic = topic.split(' - ')[-1].lower().replace(' ', '').replace('-', '')
            file_topics[normalized_topic] = f

# Step 2: Update index.html
with open(os.path.join(directory, 'index.html'), 'r') as f:
    index_content = f.read()

def replace_href(match):
    full_match = match.group(0)
    old_href = match.group(1)
    title_text = match.group(2)
    
    normalized_title = title_text.lower().replace(' ', '').replace('-', '')
    
    new_href = old_href
    if normalized_title in file_topics:
        new_href = file_topics[normalized_title]
    else:
        # fuzzy match
        for key, val in file_topics.items():
            if normalized_title in key or key in normalized_title:
                new_href = val
                break
                
    return full_match.replace(f'href="{old_href}"', f'href="{new_href}"')

# Match <a href="..."> ... <h3>Title</h3>
new_content = re.sub(r'<a href="([^"]+)" class="card\s*">.*?<h3>([^<]+)</h3>', replace_href, index_content, flags=re.DOTALL)

with open(os.path.join(directory, 'index.html'), 'w') as f:
    f.write(new_content)
    
print("Updated index.html")
