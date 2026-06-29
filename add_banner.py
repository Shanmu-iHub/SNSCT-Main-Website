import glob

html = """        <!-- Admission Banner Section -->
        <section class="py-16 relative overflow-hidden" style="background-color: #B91C1C;">
            <div class="absolute top-0 left-0 w-64 h-64 bg-white/5 rounded-full blur-3xl -translate-x-1/2 -translate-y-1/2 pointer-events-none"></div>
            <div class="absolute bottom-0 right-0 w-80 h-80 bg-black/10 rounded-full blur-3xl translate-x-1/3 translate-y-1/3 pointer-events-none"></div>
            <div class="container mx-auto px-6 relative z-10 text-center">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4">Admission <span class="text-yellow-400">2026</span></h2>
                <p class="text-white/90 text-lg md:text-xl max-w-3xl mx-auto mb-8">
                    Join India's most innovative engineering college. Limited seats available for<br>
                    <span class="font-bold">17 UG Programs, 3 PG Programs</span>, and <span class="font-bold">5 PhD Programs</span>
                </p>
                <div class="flex flex-wrap justify-center gap-4 mb-10">
                    <a href="tel:9003655855" class="px-6 py-3 border-2 border-white/30 text-white rounded-full font-semibold hover:bg-white/10 transition flex items-center space-x-2">
                        <i class="fas fa-phone-alt text-sm"></i>
                        <span>Call: 9003655855</span>
                    </a>
                    <a href="https://main.snsgroups.com/EnquiryNow/" class="px-6 py-3 bg-white text-[#B91C1C] rounded-full font-semibold hover:bg-gray-100 transition shadow-lg flex items-center space-x-2">
                        <i class="fas fa-edit text-sm"></i>
                        <span>Apply Now 2026</span>
                    </a>
                </div>
                <div class="bg-white/10 border border-white/20 rounded-xl p-6 max-w-2xl mx-auto backdrop-blur-sm">
                    <h4 class="text-white font-bold text-xl mb-2 flex items-center justify-center">
                        <i class="fas fa-user-graduate text-yellow-400 mr-2"></i>
                        70+ Lakh Scholarships Available
                    </h4>
                    <p class="text-white/80 text-sm">
                        Merit-based scholarships, work-while-learn programs, and financial<br> aid for deserving students
                    </p>
                </div>
            </div>
        </section>
        <!-- Footer -->"""

for f in glob.glob("*.html"):
    with open(f, "r") as file:
        content = file.read()
    
    if "<!-- Admission Banner Section -->" not in content:
        content = content.replace("        <!-- Footer -->", html)
        with open(f, "w") as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Skipped {f}")
