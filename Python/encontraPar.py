
minha_lista = [1, 2, 3, 4, 5]

for elemento in minha_lista:
	if elemento % 2 == 0:
		print("Par:", elemento)
		print("break")
		break
	else:
		print("Ímpar:", elemento)




minha_lista = [1, 2, 3, 4, 5]

for elemento in minha_lista:
	if elemento % 2 == 0:
		print("continue")
		continue
	print("Ímpar:", elemento)
