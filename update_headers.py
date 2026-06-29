import os
import glob

html_files = glob.glob('/Users/user/Downloads/SNSCT Landing/*.html')

new_header = """    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-180655129-1" data-skip-moving="true"></script>
    <script data-skip-moving="true">window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments)}; gtag("js", new Date()); gtag("config", "UA-180655129-1");</script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-R7B23MC26R" data-skip-moving="true"></script>
    <script data-skip-moving="true">window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments)}; gtag("js", new Date()); gtag("config", "G-R7B23MC26R");</script>
    <script data-skip-moving="true">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'}); var f=d.getElementsByTagName(s)[0], j=d.createElement(s), dl=l!='dataLayer'?'&l='+l:''; j.async=true; j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl; f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-NSB32RW');</script>
    <script data-skip-moving="true">!function(f,b,e,v,n,t,s) {if(f.fbq)return;n=f.fbq=function(){n.callMethod? n.callMethod.apply(n,arguments):n.queue.push(arguments)}; if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.agent='plbitrix'; n.queue=[];t=b.createElement(e);t.async=!0; t.src=v;s=b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t,s)}(window, document,'script', 'https://connect.facebook.net/en_US/fbevents.js'); fbq('init', '153788363108861'); fbq('track', 'PageView');</script>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, width=device-width">
    <meta name="HandheldFriendly" content="true">
    <meta name="MobileOptimized" content="width">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <title>SNS College of Technology | Autonomous | NAAC A++ | AI Engineering | Coimbatore | TNEA 2726</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="keywords" content="best engineering college in coimbatore, engineering colleges in coimbatore top 10, list of engineering college in coimbatore, engineering college of coimbatore, engineering colleges in coimbatore list, Ranking, Admission and Placement" />
    <meta name="description" content="SNS College of Technology, Coimbatore — Autonomous, NAAC A++, NBA. B.Tech in AI, Data Science, Generative AI. Highest package 53 LPA. TNEA Code 2726. Admissions open 2026." />
    <script data-skip-moving="true">(function() {const canvas = document.createElement('canvas');let gl;try{gl = canvas.getContext('webgl2') || canvas.getContext('webgl') || canvas.getContext('experimental-webgl');}catch (e){return;}if (!gl){return;}const result = {vendor: gl.getParameter(gl.VENDOR),renderer: gl.getParameter(gl.RENDERER),};const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');if (debugInfo){result.unmaskedVendor = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);result.unmaskedRenderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);}function isLikelyIntegratedGPU(gpuInfo){const renderer = (gpuInfo.unmaskedRenderer || gpuInfo.renderer || '').toLowerCase();const vendor = (gpuInfo.unmaskedVendor || gpuInfo.vendor || '').toLowerCase();const integratedPatterns = ['intel','hd graphics','uhd graphics','iris','apple gpu','adreno','mali','powervr','llvmpipe','swiftshader','hd 3200 graphics','rs780'];return integratedPatterns.some(pattern => renderer.includes(pattern) || vendor.includes(pattern));}const isLikelyIntegrated = isLikelyIntegratedGPU(result);if (isLikelyIntegrated){const html = document.documentElement;html.classList.add('bx-integrated-gpu', '--ui-reset-bg-blur');}})();</script>"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the block to replace
    # We want to replace from <head> to the end of the WebGL script: html.classList.add("bx-integrated-gpu", "--ui-reset-bg-blur"); } })(); </script>
    import re
    
    # We will search for <head> and then find the script that ends with bx-integrated-gpu...
    # Since the original files have varying whitespace, regex is best.
    pattern = re.compile(r'(<head>)(.*?)(<script data-skip-moving="true">[^<]+bx-integrated-gpu.*?<\/script>)', re.DOTALL)
    
    match = pattern.search(content)
    if match:
        new_content = content[:match.start(2)] + '\n' + new_header + '\n' + content[match.end(3):]
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Pattern not found in {filepath}")

