class Gato:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

meu_cachoro = Gato("Dobby", 10)
meu_gato.nome
meu_gato.peso
meu_gato.nome = "Dobbynho"

class Cachorro:
    # Atributos de classe
    reino = "Animalia"
    especie = "Canis lupus"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

Cachorro.reino
Cachorro.reino = "Novo reino"
del Cachorro.reino


class Cao:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        print("au-au. Meu nome é {self.nome}")


# Criar a instância
meu_cachorro = Cachorro("Nora", 10)

# Chamar o método
meu_cachorro.latir()


class Circulo:
    def __init__(self):
        self.raio = 1

class Circulo2:
    def __init__(self, raio=1):
        self.raio = raio