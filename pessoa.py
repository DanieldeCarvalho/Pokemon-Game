import random
from pokemon import *

NOMES = ['Guilherme', 'Patricia', 'João', 'Matheus', 'Maria', 'Antonio',
         'Gustavo', 'Marcelo', 'Lorena', 'Miguel']

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Flarion'),
    PokemonFogo('charmilion'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Magicarp'),
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):  # pokemon igual a lista
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não tem nenhum pokemon.')

class Player(Pessoa):
    tipo = 'Player'

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} Capturou {pokemon}')

class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons: # se nao tiver pokemons
            for i in range(random.randint(1, 6)): # quero que o inimigo tenha de 1 a 6 pokemons
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons) # chama a funcao de inicializar superior
