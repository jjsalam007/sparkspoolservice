import os
import shutil


header= '''
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RP1VG2H53D"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-RP1VG2H53D');
</script></head>
'''

for d in os.listdir('pool-repair'):
    try:
        for c in os.listdir(f'pool-repair/{d}'):
            try:
                for b in os.listdir(f'pool-repair/{d}/{c}'):
                    try:
                        search_categories = open(f'pool-repair/{d}/{c}/{b}', "r", encoding="utf8").read()
                        
                        op= search_categories.replace("﻿", '').replace('</head>', header, 1)
                        
                        fp = open(f'pool-repair/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except:
                        pass
            except:
                pass
    except:
        pass
    
for d in os.listdir('pool-repair'):
    try:
        search_categories = open(f'pool-repair/{d}/index.html', "r", encoding="utf8").read()
        
        op= search_categories.replace("﻿", '').replace('</head>', header, 1)
        
        fp = open(f'pool-repair/{d}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(op)
        fp.close()
    except:
        pass

try:
    search_categories = open(f'pool-repair/index.html', "r", encoding="utf8").read()
    
    op= search_categories.replace("﻿", '').replace('</head>', header, 1)
    
    fp = open(f'pool-repair/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass




