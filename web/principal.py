from leitor_html import analizar_html
from leitor_js import analizar_js



html = open('index.html')
print('No HTML')
analizar_html(html)

print('\nNo JS')
js = open('script.js')
analizar_js(js)