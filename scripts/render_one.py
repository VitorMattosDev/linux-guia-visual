import sys, os
from playwright.sync_api import sync_playwright
html = os.path.abspath(sys.argv[1])
outpng = os.path.abspath(sys.argv[2])
outpdf = outpng.rsplit('.',1)[0] + '.pdf'
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto('file://' + html)
    pg.wait_for_timeout(400)
    pg.pdf(path=outpdf, format='A4', print_background=True,
           margin={'top':'0','bottom':'0','left':'0','right':'0'})
    # screenshot A4 @ ~140dpi for visual check
    pg.set_viewport_size({'width':1160,'height':1640})
    pg.screenshot(path=outpng, full_page=True)
    b.close()
print('ok', outpdf, outpng)
