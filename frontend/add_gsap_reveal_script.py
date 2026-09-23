import os
import glob

script_to_add = """
    <script>
        // Reveal elements using GSAP
        setTimeout(() => {
            const reveals = document.querySelectorAll('.gsap-reveal');
            reveals.forEach((el) => {
                gsap.fromTo(el, 
                    { opacity: 0, y: 50, visibility: 'hidden' }, 
                    {
                        scrollTrigger: {
                            trigger: el,
                            start: "top 85%",
                            toggleActions: "play none none none"
                        },
                        opacity: 1,
                        y: 0,
                        visibility: 'visible',
                        duration: 1,
                        ease: "power2.out"
                    }
                );
            });
        }, 100);
    </script>
</body>"""

service_files = glob.glob("/home/dilli/OM -AI/frontend/services/*/index.html")

for filepath in service_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script>' not in content.split('</footer>')[-1]:
        # Replace the final </body> with the script + </body>
        content = content.replace('</body>', script_to_add)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Added GSAP reveal script to {len(service_files)} service pages.")
