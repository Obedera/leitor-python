def analizar_html(html):
    texto_html = html.read()
    linha_html = texto_html.splitlines()
    contador_linha_html = 0

    while contador_linha_html<len(linha_html):
        palavras = linha_html[contador_linha_html].split()
        for j in palavras:
            if j == '<bodyy>':
                print(f'Tem erro na linha {contador_linha_html+1} o "{j}" está escrito errado')
                
            if j == '<scripts':
                print(f'Tem erro na linha {contador_linha_html+1} o "{j}" está escrito errado')    
        contador_linha_html += 1