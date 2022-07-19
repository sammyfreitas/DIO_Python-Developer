#fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

#fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#potencia
def encontrar_potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * encontrar_potencia(a, b-1)