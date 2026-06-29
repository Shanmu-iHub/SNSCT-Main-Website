import os
import glob

# The new content to insert
new_content = """        <!-- Admission 2025 CTA Section -->
        <section class="section-padding gradient-bg relative overflow-hidden">
            <div class="absolute inset-0 opacity-10">
                <div class="absolute top-0 left-0 w-96 h-96 bg-white rounded-full blur-3xl"></div>
                <div class="absolute bottom-0 right-0 w-96 h-96 bg-yellow-300 rounded-full blur-3xl"></div>
            </div>

            <div class="container mx-auto px-6 text-center relative z-10">
                <h2 class="font-display text-5xl md:text-7xl font-bold text-white mb-8">
                    Admission <span class="text-yellow-300">2026</span>
                </h2>
                <p class="text-2xl text-white mb-12 max-w-4xl mx-auto leading-relaxed">
                    Join India's most innovative engineering college. Limited
                    seats available for <br />
                    <strong>17 UG Programs</strong>,
                    <strong>3 PG Programs</strong>, and
                    <strong>5 PhD Programs</strong>



                </p>

                <div
                    class="flex flex-col md:flex-row items-center justify-center space-y-6 md:space-y-0 md:space-x-8 mb-10">
                    <button
                        class="btn-secondary border-white text-white hover:bg-white hover:text-white text-xl px-12 py-4">
                        <i class="fas fa-phone"></i>
                        Call: 9003655855
                    </button>
                    <button class="btn-primary text-xl px-12 py-4 bg-white text-red-600 hover:bg-yellow-300">
                        <i class="fas fa-edit"></i>
                        <a href="https://main.snsgroups.com/EnquiryNow/" target="_blank">
                            Apply Now 2026
                        </a>
                    </button>
                </div>

                <!-- Scholarship Info -->
                <div class="glass-effect rounded-3xl p-8 max-w-2xl mx-auto">
                    <h3 class="font-display text-3xl font-bold text-white mb-4">
                        <i class="fas fa-graduation-cap text-yellow-300 mr-3"></i>
                        70+ Lakh Scholarships Available
                    </h3>
                    <p class="text-white text-lg">
                        Merit-based scholarships, work-while-learn programs, and
                        financial aid for deserving students
                    </p>
                </div>
            </div>
        </section>

        <!-- Footer -->"""

import re

for filepath in glob.glob("*.html"):
    if filepath == "index.html":
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to find everything from the first "<!-- Admission Banner Section -->" 
    # to the start of "<!-- Footer -->" (inclusive of any extra banners if they exist)
    # Wait, the previous successful files might have "<!-- Admission 2025 CTA Section -->". Let's handle both.
    
    # 1. Strip out ANY admission banners or CTA sections and the footer marker
    # We will look for anything starting with <!-- Admission Banner Section --> or <!-- Admission 2025 CTA Section -->
    # up to <!-- Footer --> and replace it entirely.
    
    pattern = re.compile(r'(?:<!-- Admission Banner Section -->|<!-- Admission 2025 CTA Section -->).*?<!-- Footer -->', re.DOTALL)
    
    if pattern.search(content):
        new_text = pattern.sub(new_content, content)
        with open(filepath, 'w') as f:
            f.write(new_text)
        print(f"Updated {filepath}")
    else:
        print(f"No match found in {filepath}")

