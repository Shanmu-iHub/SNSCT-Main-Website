import os
import glob

html_files = glob.glob("/Users/user/Downloads/SNSCT Landing/*.html")

mobile_nav_html = """
    <!-- Mobile Bottom Navigation -->
    <div
        class="fixed bottom-0 left-0 w-full bg-white shadow-[0_-4px_10px_rgba(0,0,0,0.05)] z-50 md:hidden flex justify-between items-end px-2 pb-5 pt-2 rounded-t-2xl">
        <!-- Home -->
        <a href="index.html" class="flex flex-col items-center justify-center w-1/5 pb-1 text-red-700">
            <i class="fas fa-home text-xl mb-1"></i>
            <span class="text-[10px] font-semibold mt-1">Home</span>
        </a>

        <!-- Placements -->
        <a href="https://snsct.org/old/Placement_cell.html" target="_blank"
            class="flex flex-col items-center justify-center w-1/5 pb-1 text-gray-400 hover:text-red-700 transition-colors">
            <i class="fas fa-chart-line text-xl mb-1"></i>
            <span class="text-[10px] font-medium mt-1">Placements</span>
        </a>

        <!-- Apply (Floating/Prominent) -->
        <div class="w-1/5 flex flex-col items-center justify-end relative pb-1">
            <a href="https://main.snsgroups.com/EnquiryNow/" target="_blank"
                class="absolute bottom-6 flex items-center justify-center bg-red-700 w-14 h-14 rounded-full text-white shadow-lg border-4 border-white transform transition hover:scale-105 active:scale-95 z-10">
                <i class="fas fa-pen-to-square text-2xl"></i>
            </a>
            <span class="text-[10px] font-medium text-gray-400 mt-1">Apply</span>
        </div>

        <!-- About Us -->
        <a href="about.html"
            class="flex flex-col items-center justify-center w-1/5 pb-1 text-gray-400 hover:text-red-700 transition-colors">
            <i class="fas fa-info-circle text-xl mb-1"></i>
            <span class="text-[10px] font-medium mt-1">About</span>
        </a>

        <!-- Contact Us -->
        <a href="contact.html"
            class="flex flex-col items-center justify-center w-1/5 pb-1 text-gray-400 hover:text-red-700 transition-colors">
            <i class="fas fa-phone-alt text-xl mb-1"></i>
            <span class="text-[10px] font-medium mt-1">Contact</span>
        </a>
    </div>
    <!-- Ensure body doesn't overlap with fixed bottom nav -->
    <div class="h-24 md:hidden"></div>
"""

padding_style = """
    <style>
        @media (max-width: 768px) {
            body {
                padding-top: 50px !important;
            }
        }
    </style>
"""

for file_path in html_files:
    if 'bitrix.html' in file_path:
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate injection
    if 'padding-top: 50px !important;' not in content:
        content = content.replace('</head>', padding_style + '</head>')
        
    if 'Mobile Bottom Navigation' not in content:
        content = content.replace('</body>', mobile_nav_html + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Updated HTML files.")
