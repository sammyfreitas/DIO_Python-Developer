minha_lista = [1, 2, 3, 4, 5]

for elem in minha_lista:
    if elem > 6:
        print("Encontrado")
        break
else:
    print("Não encontrado")

minha_lista = [1, 2, 3, 4, 5, 8] # Agora a lista tem o valor 8

for elem in minha_lista:
    if elem > 6:
        print("Encontrado")
        break
else:
    print("Não encontrado")