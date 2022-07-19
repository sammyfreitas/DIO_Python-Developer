for i in range(5):
    print(i)

for num in range(8):
	print("Olá" * num)

minha_lista = ["a", "b", "c", "d"]
for i in range(len(minha_lista)):
	print(minha_lista[i])

mensagem = "Olá, mundo!"

for char in mensagem:
	print(char)

word = "Hello"

for char in word.lower(): # calling the string method
	print(char)

palavra = "Olá"

for char in palavra.upper(): # chamando o método de string
	print(char)


minha_lista = (2, 3, 4, 5)

for num in minha_lista:
	if num % 2 == 0:
		print("Par")
	else:
		print("Ímpar")


x = 6

while x < 15:
	print(x)
	x += 1

x = 4
while x >= 0:
	print("Olá" * x)
	x -= 1

num = 5
while num >= 1:
	print("*" * num)
	num -= 2

x = 5
while x < 15:
	if x % 2 == 0:
		x += 1
		continue
	print("Ímpar:", x)
	x += 1

#laços aninhados

for i in range(3):
	for j in range(2):
		print(i, j)

for i in range(3):
	print("===> Laço externo")
	print(f"i = {i}")
	for j in range(2):
		print("Laço interno")
		print(f"j = {j}")

num_linhas = 5
for i in range(5):
	for num_colunas in range(num_linhas-i):
		print("*", end="")
	print()

i = 5

while i > 0:
	j = 0
	while j < 2:
		print(i, j)
		j += 1
	i -= 1


def boasvindas_estudante(nome):
    print(f"Olá, {nome}! Boas-vindas à aula.")


def imprimir_padrao(num_linhas, caractere):
	for i in range(num_linhas):
		for num_colunas in range(num_linhas-i):
			print(caractere, end="")
		print()

imprimir_padrao(5, "A")
imprimir_padrao(8, "%")
imprimir_padrao(10, "#")