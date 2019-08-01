from googletrans import Translator
translator = Translator()
try:
    nome = 'Obede'
    if nome == 'Obede':
        print(nome)
        print(sobrenome)

except Exception as erro:
    arq = open('texto.txt', 'w')
    texto = str(erro)
    contador = 0
    posicao = 0
    while contador<len(texto):
        if texto[contador] == "'":
            posicao = contador
        contador += 1

    texto_traduzir = texto[posicao+1:]
    texto_traduzido = translator.translate(texto_traduzir,dest='pt').text
    arq.write(f'Erro aqui {texto[5:posicao+1]} {texto_traduzido}')
    arq.close()
    print(f'Erro aqui {texto[5:posicao+1]} {texto_traduzido}')
