import os
import glob

html_files = glob.glob("/Users/user/Downloads/SNSCT Landing/*.html")

for file_path in html_files:
    if 'bitrix.html' in file_path:
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Expand any standard container width
    content = content.replace(
        '<div class="container mx-auto px-6 text-center relative z-10">',
        '<div class="container mx-auto px-6 text-center relative z-10 max-w-[1600px]">'
    )
    content = content.replace(
        '<div class="container mx-auto px-6">',
        '<div class="container mx-auto px-6 max-w-[1600px]">'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated widths across more containers.")
