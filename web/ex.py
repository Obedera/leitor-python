html = open('index.html')
texto_html = html.read()
linha_html = texto_html.splitlines()
js = open('script.js')
texto_js = js.read()
linha_js = texto_js.splitlines()
contador_linha_html = 0
contador_linha_js = 0

while contador_linha_html<len(linha_html):
    palavras = linha_html[contador_linha_html].split()
    for j in palavras:
        if j == '<bodyy>':
            print(f'Tem erro na linha {contador_linha_html+1} o "{j}" está escrito errado')
            
        if j == '<scripts':
            print(f'Tem erro na linha {contador_linha_html+1} o "{j}" está escrito errado')
            
    contador_linha_html += 1

while contador_linha_js<len(linha_js):
    palavras = linha_js[contador_linha_js].split()
    for j in palavras:
        if j[:3] == 'ale':
                if j[3:6] != 'rt(':
                    print(f'Tem erro na linha "{contador_linha_js+1}" o "{j}" está escrito errado')
                if j[(len(j)-1):]==')':
                    print(f'Não se esqueça de colocar um ";" no "{j}" da linha {contador_linha_js+1}')
                elif j[(len(j)-2):]!=');':
                    print(f'Tem erro na linha {contador_linha_js+1} o "{j}" está escrito errado')
            
    contador_linha_js += 1


# print(linha_html.count('<bodyy>'))
# print(linha_html.count('</body>'))
