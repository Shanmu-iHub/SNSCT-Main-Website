import re

with open('/Users/user/Downloads/SNSCT Landing/contact.html', 'r') as f:
    content = f.read()

# We want to replace <form class="space-y-5"> ... </form> inside contact.html with the bitrix integration.
replacement = """
                        <!-- Loading State -->
                        <style>
                            /* Loading Animation */
                            .loading { text-align: center; padding: 10px; color: #718096; }
                            .spinner { border: 3px solid #f3f4f6; border-top: 3px solid #C80F61; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 16px; }
                            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                            
                            /* Bitrix Styles */
                            .b24-form-wrapper { background: transparent !important; border: none !important; padding: 0 !important; box-shadow: none !important; margin: 0 !important; }
                            .b24-form-header { display: none !important; }
                            .b24-form-field { margin-bottom: 20px !important; position: relative !important; padding-bottom: 0 !important;}
                            .b24-form-separator, .b24-form-field-separator, .b24-form-field-shadow, .b24-form-control-shadow, .b24-form-field-line, .b24-form-control-line, .b24-form-field-line-1, .b24-form-field-line-2, .b24-form-field-line-3, [class*="b24-form-field-line"], [class*="b24-form-control-line"], .b24-form-field::before, .b24-form-field::after, .b24-form-control::before, .b24-form-control::after { display: none !important; content: none !important; height: 0 !important; border: none !important; position: absolute !important; opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; z-index: -1 !important; }
                            .b24-form-control-label { position: absolute !important; opacity: 0 !important; pointer-events: none !important; }
                            .b24-form-control, select.b24-form-control { width: 100% !important; background: #F8F9FA !important; border: 1px solid #e5e7eb !important; border-radius: 12px !important; padding: 14px 18px !important; font-size: 14px !important; font-family: 'Poppins', sans-serif !important; color: #1f2937 !important; box-shadow: none !important; transition: all 0.3s ease !important; appearance: none !important; -webkit-appearance: none !important; -moz-appearance: none !important; }
                            .b24-form-control::placeholder { color: #9ca3af !important; font-weight: 400 !important; }
                            .b24-form-control:focus { border-color: #ef4444 !important; background: #ffffff !important; outline: none !important; box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1) !important; }
                            .b24-form-dropdown { border-radius: 12px !important; border: 2px solid transparent !important; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05) !important; background: white !important; }
                            .b24-form-dropdown-item { padding: 12px 18px !important; font-size: 14px !important; font-family: 'Poppins', sans-serif !important; color: #4b5563 !important; transition: all 0.2s ease !important; }
                            .b24-form-dropdown-item:hover { background: #f3f4f6 !important; color: #ef4444 !important; }
                            .b24-form-btn { width: 100% !important; margin-top: 10px !important; padding: 16px 24px !important; border-radius: 12px !important; background: #C80F61 !important; color: #ffffff !important; font-size: 16px !important; font-weight: 700 !important; border: none !important; font-family: 'Poppins', sans-serif !important; cursor: pointer !important; transition: all 0.3s ease !important; letter-spacing: 0.025em !important; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important; }
                            .b24-form-btn:hover { transform: translateY(-2px) !important; background: #b91c1c !important; }
                            .b24-form-btn:active { transform: translateY(0) !important; }
                            #bitrix-form-container { position: relative; z-index: 1000; }
                            .b24-form-control-required-symbol { color: #ff4d4d !important; }
                            [class*="line"], [class*="shadow"] { box-shadow: none !important; border: none !important; }
                            .b24-form-control-shadow, .b24-form-field-shadow, .b24-form-shadow, .b24-form-field-line, .b24-form-control-line, .b24-form-field-line-1, .b24-form-field-line-2 { display: none !important; height: 0 !important; overflow: hidden !important; }
                            .b24-form { padding-top: 0 !important; margin-top: 0 !important; }
                            .b24-form-sign { margin-top: 24px !important; font-size: 12px !important; color: #9ca3af !important; text-align: center !important; }
                        </style>

                        <div class="loading" id="loading">
                            <div class="spinner"></div>
                            <p>Loading form...</p>
                        </div>

                        <!-- Bitrix24 Form -->
                        <div id="bitrix-form-container"></div>
                        <script data-b24-form="inline/52/2qc8ap" data-skip-moving="true" async
                            src="https://cdn.bitrix24.com/b11752903/crm/form/loader_52.js"></script>

                        <script>
                            setTimeout(function () {
                                var loading = document.getElementById('loading');
                                if (loading) {
                                    loading.style.display = 'none';
                                }
                            }, 3000);

                            const snsColleges = [
                                "SNS College of Technology"
                            ];

                            function applyFormFixes() {
                                const fields = document.querySelectorAll('.b24-form-field');
                                fields.forEach(field => {
                                    const label = field.querySelector('.b24-form-control-label');
                                    const input = field.querySelector('.b24-form-control');
                                    const container = field;

                                    field.querySelectorAll('[class*="line"]').forEach(line => {
                                        line.style.setProperty('display', 'none', 'important');
                                        line.style.setProperty('opacity', '0', 'important');
                                        line.style.setProperty('height', '0', 'important');
                                    });

                                    if (label) {
                                        const text = label.textContent.trim();
                                        if (text.includes('Admission To Grade')) {
                                            container.style.display = 'none';
                                            return;
                                        }

                                        if (text.includes('SNSACD') || text.includes('SNS Academy') || text.includes('CBSE SCHOOL')) {
                                            label.textContent = "Choose College *";
                                            if (input && input.tagName !== 'SELECT' && !input.dataset.replaced) {
                                                const select = document.createElement('select');
                                                select.className = input.className;
                                                select.name = input.name;
                                                select.required = true;
                                                select.dataset.replaced = "true";
                                                select.innerHTML = '<option value="">Choose College *</option>' + snsColleges.map(c => `<option value="${c}" selected>${c}</option>`).join('');
                                                input.parentNode.replaceChild(select, input);
                                                select.addEventListener('change', (e) => {
                                                    const event = new Event('input', { bubbles: true });
                                                    select.dispatchEvent(event);
                                                });
                                            }
                                            return;
                                        }

                                        if (text.includes('Name of the Child')) {
                                            label.textContent = text.replace('Name of the Child', 'Name of the Candidate');
                                            if (input && input.tagName !== 'SELECT') {
                                                let required = text.includes('*');
                                                input.placeholder = 'Name of the Candidate' + (required ? ' *' : '');
                                            }
                                        }

                                        if (text.includes('Parent Name')) {
                                            label.textContent = text.replace('Parent Name', 'Parent / Guardian Name');
                                            if (input && input.tagName !== 'SELECT') {
                                                let required = text.includes('*');
                                                input.placeholder = 'Parent / Guardian Name' + (required ? ' *' : '');
                                            }
                                        }

                                        if (input && input.tagName !== 'SELECT' && !input.placeholder) {
                                            let cleanText = text.replace(/\s*\*$/, '').trim();
                                            let required = text.includes('*');
                                            input.placeholder = required ? cleanText + ' *' : cleanText;
                                        }
                                    }
                                });
                            }

                            const observer = new MutationObserver((mutations) => {
                                mutations.forEach((mutation) => {
                                    if (mutation.addedNodes.length) applyFormFixes();
                                });
                            });

                            const target = document.getElementById('bitrix-form-container');
                            if (target) observer.observe(target, { childList: true, subtree: true });

                            applyFormFixes();
                            setInterval(applyFormFixes, 1000);
                        </script>
"""

new_content = re.sub(r'<form class="space-y-5">.*?</form>', replacement, content, flags=re.DOTALL)

with open('/Users/user/Downloads/SNSCT Landing/contact.html', 'w') as f:
    f.write(new_content)

print("Form replaced successfully!")
