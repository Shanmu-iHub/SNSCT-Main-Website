import os
import glob

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We want to replace 'bottom: 0.5rem;' with 'bottom: 6rem;' inside .floating-chat-container
    original_str = """        .floating-chat-container {
            position: fixed;
            bottom: 0.5rem;
            right: 1rem;"""
            
    new_str = """        .floating-chat-container {
            position: fixed;
            bottom: 6rem;
            right: 1rem;"""

    if original_str in content:
        content = content.replace(original_str, new_str)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        # Just in case the indentation differs slightly
        original_str2 = """        .floating-chat-container {
            position: fixed;
            bottom: 5rem;"""
        if "bottom: 0.5rem;" in content and ".floating-chat-container" in content:
            # Let's use a simpler replace just in case
            parts = content.split('.floating-chat-container {')
            if len(parts) > 1:
                sub_parts = parts[1].split('}', 1)
                if 'bottom: 0.5rem;' in sub_parts[0]:
                    new_sub = sub_parts[0].replace('bottom: 0.5rem;', 'bottom: 6rem;')
                    content = parts[0] + '.floating-chat-container {' + new_sub + '}' + sub_parts[1]
                    with open(filepath, 'w') as f:
                        f.write(content)
                    print(f"Updated {filepath} (using fallback method)")
