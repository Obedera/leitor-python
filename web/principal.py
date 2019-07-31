from leitor_html import analizar_html
from leitor_js import analizar_js



print('---------No HTML---------')
html = open('index.html')
print(analizar_html(html))

print('\n---------No JS---------')
js = open('script.js')
print(analizar_js(js))