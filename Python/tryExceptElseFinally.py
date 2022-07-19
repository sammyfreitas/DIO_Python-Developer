a = int(input("Insira a: "))
b = int(input("Insira b: "))

try:
    divisao = a / b
    print(divisao)
except:
    print("Insira valores válidos.")


indice = int(input("Insira o índice: "))
try:
    minha_lista = [1, 2, 3, 4]
    print(minha_lista[índice])
except IndexError: # especifica o tipo
    print("Insira um índice válido.")


a = int(input("Insira a: "))
b = int(input("Insira b: "))

try:
    divisao = a / b
    print(divisao)
except ZeroDivisionError: # especifica o tipo
    print("Insira valores válidos.")

indice = int(input("Insira o índice: "))
try:
    minha_lista = [1, 2, 3, 4]
    print(minha_lista[indice])
except IndexError as e:
    print("Exceção causada:", e)


a = int(input("Insira a: "))
b = int(input("Insira b: "))
try:
    divisao = a / b
    print(divisao)
except ZeroDivisionError as err:
    print("Insira valores válidos.", err)


a = int(input("Insira a: "))
b = int(input("Insira b: "))

try:
    divisao = a / b
    print(divisao)
except ZeroDivisionError as err:
    print("Insira valores válidos.", err)
else:
    print("Os dois valores eram válidos.")



a = int(input("Insira a: "))
b = int(input("Insira b: "))

try:
    divisao = a / b
    print(divisao)
except ZeroDivisionError as err:
    print("Insira valores válidos.", err)
else:
    print("Os dois valores eram válidos.")
finally:
    print("O programa terminou!")