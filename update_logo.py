import os
import glob
import re

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check if it's already wrapped to avoid double wrapping
    if '<a href="index.html"><img src="https://snsct.snscourseware.org/images/logo%20copy.png"' in content:
        continue

    # Regex to match the img tag
    pattern = re.compile(r'(<img[^>]+src="https://snsct\.snscourseware\.org/images/logo%20copy\.png"[^>]+logo-image[^>]+>)')
    
    def replacer(match):
        return f'<a href="index.html">{match.group(1)}</a>'
        
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
