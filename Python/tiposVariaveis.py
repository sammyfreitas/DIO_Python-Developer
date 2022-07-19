>>> type(1)
<class 'int'>

>>> type(15)
<class 'int'>

>>> type(0)
<class 'int'>

>>> type(-46)
<class 'int'>

>>> type(4.5)
<class 'float'>

>>> type(5.8)
<class 'float'>

>>> type(2342423424.3)
<class 'float'>

>>> type(4.0)
<class 'float'>

>>> type(0.0)
<class 'float'>

>>> type(-23.5)
<class 'float'>

>>> complex(4, 5)
(4+5j)

>>> complex(6, 8)
(6+8j)

>>> complex(3.4, 3.4)
(3.4+3.4j)

>>> complex(0, 0)
0j

>>> complex(5)
(5+0j)

>>> complex(0, 4)
4j

>>> minha_string = "Hello"

>>> minha_string[0]
'H'

>>> minha_string[1]
'e'

>>> minha_string[2]
'l'

>>> minha_string[3]
'l'

>>> minha_string[4]
'o'

nome = "Nora"
linguagem_favorita = "Python"

print(f"Olá, eu sou {nome}. Estou aprendendo {linguagem_favorita}.")
valor = 5

print(f"{valor} multiplicado por 2 é: {valor * 2}")


freecodecamp = "FREECODECAMP"

print(f"{freecodecamp.lower()}")


>>> type(True)
<class 'bool'>

>>> type(False)
<class 'bool'>

>>> type(true)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined

>>> type(false)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    type(false)
NameError: name 'false' is not defined


# Tabuleiro simples, onde: 
# 0 = Bloco vazio
# 1 = Moeda
# 2 = Inimigo
# 3 = Objetivo
tabuleiro = [[0, 0, 1],
             [0, 2, 0],
             [1, 0, 3]]


>>> letras = ["a", "b", "c", "d"]

>>> letras[0] = "z"

>>> letras
['z', 'b', 'c', 'd']

>>> minha_lista = [1, 2, 3, 4]

>>> minha_lista.remove(3)

>>> minha_lista
[1, 2, 4]