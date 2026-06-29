import os
import glob

html_files = glob.glob("/Users/user/Downloads/SNSCT Landing/*.html")

for file_path in html_files:
    if 'bitrix.html' in file_path:
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the main section wrappers
    # `<div class="container mx-auto px-6 relative z-10">`
    # `<div class="container mx-auto px-6 relative z-10 max-w-7xl">`
    
    # We will just replace all variations with max-w-[1600px]
    content = content.replace(
        '<div class="container mx-auto px-6 relative z-10 max-w-7xl">',
        '<div class="container mx-auto px-6 relative z-10 max-w-[1600px]">'
    )
    
    content = content.replace(
        '<div class="container mx-auto px-6 relative z-10 max-w-screen-xl">',
        '<div class="container mx-auto px-6 relative z-10 max-w-[1600px]">'
    )

    # Some pages might just have the base one
    content = content.replace(
        '<div class="container mx-auto px-6 relative z-10">',
        '<div class="container mx-auto px-6 relative z-10 max-w-[1600px]">'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated widths across all pages to max-w-[1600px].")
