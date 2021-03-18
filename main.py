from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, você pdoer[a escolher agora o pokemon que irálhe acompanhar nesta jornada!')

    pikachu = PokemonEletrico('Pikachu', level= 1)
    charmander = PokemonFogo('Charmander', level= 1)
    squirtle  = PokemonAgua('Squirtle', level= 1)

    print('Qual pokemon você deseja?: ')
    print('1 -', pikachu)
    print('2 -', charmander)
    print('3 -', squirtle)

    while True:
        escolha = input('Escolha o seu pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        if escolha == '2':
            player.capturar(charmander)
            break
        if escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('escolha inválida')

# escolher_pokemon_inicial(player)


player = Player('Daniel')
player.capturar(PokemonFogo('Charmander', level=1))

inimigo1 = Inimigo(nome='Gary', pokemons=(PokemonAgua('Squirtle', level=1)))
print(inimigo1)
inimigo1.mostrar_pokemons()

# 01:29:34
# fazer a funcao batalhar