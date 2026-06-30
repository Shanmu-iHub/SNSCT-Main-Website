import os
import glob

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # We want to replace href="https://main.snsgroups.com/EnquiryNow/" with the onclick workaround.
    original_str = 'href="https://main.snsgroups.com/EnquiryNow/" target="_blank"'
    new_str = 'href="https://main.snsgroups.com/EnquiryNow/" target="_blank" onclick="event.preventDefault(); window.open(\'https://main.snsgroups.com/EnquiryNow/\', \'_blank\');"'
    
    # Also handle instances without target="_blank" if any
    original_str2 = 'href="https://main.snsgroups.com/EnquiryNow/"'
    new_str2 = 'href="https://main.snsgroups.com/EnquiryNow/" onclick="event.preventDefault(); window.open(\'https://main.snsgroups.com/EnquiryNow/\', \'_blank\');"'

    if original_str in content:
        content = content.replace(original_str, new_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
    elif original_str2 in content and "window.open" not in content:
        # Care needed not to double replace if target="_blank" was next to it
        pass

for filepath in glob.glob("*.html"):
    process_file(filepath)
