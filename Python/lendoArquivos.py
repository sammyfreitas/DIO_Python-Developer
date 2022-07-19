with open("frases_famosas.txt") as arquivo:
    for linha in arquivo:
        print(linha)

with open("frases_famosas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)


palavras = ["Código", "Python", "Verde", "Incrível"]

with open("frases_famosas.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")


#apagar o arquivo em python
#import os

#if os.path.exists("frases_famosas.txt"):
#  os.remove("frases_famosas.txt")
#else:
#  print("O arquivo não existe")