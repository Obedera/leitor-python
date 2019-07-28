from googletrans import Translator
translator = Translator()
try:
  print(x)
except Exception as erro:
    arq = open('texto.txt', 'w')
    texto = str(erro)
    texto_traduzido = translator.translate(texto,dest='pt').text
    arq.write(texto_traduzido)
    arq.close()
