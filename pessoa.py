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
    def __init__(self, nome=None, pokemons=[], dinheiro =100):  # pokemon igual a lista
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro


    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons: #se tiver pokemons
            print(f'Pokemons de {self}:')
            for index, pokemon in enumerate(self.pokemons):
                print(f'{index} -- {pokemon}')
        else:
            print(f'{self} não tem nenhum pokemon.')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}')
            return pokemon_escolhido
        else:
            print('ERRO: este jogador não possui nenhum pokemon para ser escolhido')

    def mostrar_dinheiro(self):
        print(f'Voce possui ${self.dinheiro} em sua conta')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f"Voce ganhou ${quantidade}")
        self.mostrar_dinheiro()

    def batalhar(self, inimigo):
        print(f'{self} Iniciou uma batalha com {inimigo}')

        inimigo.mostrar_pokemons()
        pokemon_inimigo = inimigo.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f'{pokemon_inimigo} ganhou a batalha')
                    break
        else:
            print('Essa batalha não pode ocorrer')


class Player(Pessoa):
    tipo = 'Player'

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} Capturou {pokemon}')

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                escolha = input('Escolha o seu pokemon: ')
                try:
                    escolha= int(escolha)
                    pokemon_escolhido = self.pokemons[escolha] #colchetes ja que e para acessar indice
                    print(f'{pokemon_escolhido} eu escolho você!!')
                    return pokemon_escolhido
                    # escolha= int(escolha) #teste de codigo
                    # self.pokemons[escolha]
                    # print(f'{self.pokemons[escolha]} eu escolho você!')
                    # break
                except:
                    print('escolha invalida')
        else:
            print('ERRO: este jogador não possui nenhum pokemon para ser escolhido')

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f'Um pokemon selvagem apareceu: {pokemon}')

            escolha = input('Deseja capturar pokemon? (s/n):')
            if escolha == 's':
                if random.random() <= 0.3:
                    self.capturar(pokemon)
                else:
                    print(f'{pokemon} fugiu! ')
            else:
                print('Ok, boa viagem')
        else:
            print('Esta exploracao nao deu em nada')


class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons: # se nao tiver pokemons
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)): # quero que o inimigo tenha de 1 a 6 pokemons
                pokemons_aleatorios.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons) # chama a funcao de inicializar superior
        else:
            super().__init__(nome=nome, pokemons=pokemons )