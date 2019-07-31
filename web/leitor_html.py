def analizar_html(html):
    texto_html = html.read()
    linha_html = texto_html.splitlines()
    Erros = ''

    def quebrar_por_palavra(linha):
        contador_linha_html = 0
        palavras = []
        while contador_linha_html<len(linha):
            palavra = linha[contador_linha_html].split()
            for i in palavra:
                palavras.append(i)  
            contador_linha_html += 1
        return palavras

    lista_palavras = quebrar_por_palavra(linha_html)

    def quebrar_por_letra(lista_palavras):
        contador_letra_html = 0
        letras = []
        while contador_letra_html<len(lista_palavras):
            letra = lista_palavras[contador_letra_html]
            for i in letra:
                letras.append(i)
            contador_letra_html += 1
        return letras
    
    lista_letras = quebrar_por_letra(lista_palavras)

    if lista_letras.count('<') > lista_letras.count('>'):
        Erros += 'Você esqueceu de colocar ">"\n'
    if lista_letras.count('<') < lista_letras.count('>'):
        Erros += 'Você esqueceu de colocar "<"\n'

    def checar_erros_palavra(lista_palavras):
        contador = 0
        erros = ''
        while contador<len(lista_palavras):
            if lista_palavras[contador] == '<bodyy>' or lista_palavras[contador] == '<bodyy':
                erros += f'Tem erro na linha {contador+1} o "{lista_palavras[contador]}" está escrito errado\n'
                   
            if lista_palavras[contador] == '<scripts':
                erros += f'Tem erro na linha {contador+1} o "{lista_palavras[contador]}" está escrito errado\n'

            contador += 1

        return erros


    Erros += checar_erros_palavra(lista_palavras)

    return Erros
    
    
    



