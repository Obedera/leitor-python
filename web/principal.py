from leitor_html import analizar_html
from leitor_js import analizar_js



html = open('index.html')
print('---------No HTML---------')
print(analizar_html(html))

print('\n---------No JS---------')
js = open('script.js')
analizar_js(js)