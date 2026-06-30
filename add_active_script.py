import os
import glob

script_to_add = """
<script>
document.addEventListener('DOMContentLoaded', () => {
    const bottomNavLinks = document.querySelectorAll('.fixed.bottom-0 > a');
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    bottomNavLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        
        // Reset classes
        link.className = 'flex flex-col items-center justify-center w-1/5 pb-1 text-gray-400 hover:text-red-700 transition-colors';
        const span = link.querySelector('span');
        if (span) span.className = 'text-[10px] font-medium mt-1';
        
        // Active match logic
        if (href === currentPath || (currentPath === '' && href === 'index.html')) {
            link.className = 'flex flex-col items-center justify-center w-1/5 pb-1 text-red-700';
            if (span) span.className = 'text-[10px] font-semibold mt-1';
        }
    });
});
</script>
</body>
"""

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "const bottomNavLinks = document.querySelectorAll('.fixed.bottom-0 > a');" not in content:
        content = content.replace("</body>", script_to_add)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")
