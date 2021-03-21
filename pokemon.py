import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None): #<argumento>=None = argumento nao obrigatorio
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1,100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 3
        self.vida = self.level * 6


    def __str__(self):
        return (f'{self.nome} ({self.level})')

    def atacar(self, pokemon):
        pokemon.vida -= self.ataque
        print(f'{pokemon} perdeu {self.ataque} pontos de vida')

        if pokemon.vida <= 0:
            print(f'{pokemon} foi derrotado')
            return True
        else:
            return False

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print(f'{self} lançou um raio do trovão em {pokemon}')
        super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print(f'{self} jogou uma bola de fogo em {pokemon}')
        super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, pokemon):
        print(f'{self} lançou um jato de água em {pokemon}')
        super().atacar(pokemon)


# 20:06
