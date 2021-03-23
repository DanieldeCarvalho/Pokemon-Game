import pickle

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

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo: #abrindo no modo no modo inscrita e modo binario
            pickle.dump(player, arquivo) #transformando o objeto num arquivo, primeiro parametro bojeto segundo arquivo
            print('>>> Jogo salvo com sucesso! ')
    except Exception as error:
        print('Ocorreu um erro ao salvar o jogo')
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo: #abrindo no modo no modo de leitura e modo binario
            player = pickle.load(arquivo) #fazendo o caminho inverso da funcao acima, esta pegando um arquivo
            #transformando num objeto e escrevendo na minha variavel
            print('>>> Jogo carregado com sucesso! ')
            return player
    except Exception as error:
        print('Save nao encontrado')
        print(error)

def inicio_jogo():
    nome = input('Ola, qual o seu nome?:  ')
    player = Player(nome, pokemons=[], dinheiro=0)

    print(f'Ola {nome} Bem vindo ao mundo pokemon. sua missao e se tornar um metre dos pokemons')
    print('capture o maximo de pokmeons que conseguir e lute com seus inimigos')
    player.mostrar_dinheiro()

    print('Voce nao tem nenhum pokemon. portando escolha um para comecar sua jornada:')
    escolher_pokemon_inicial(player)

    print('Pronto, agora que voce ja possui um pokemon, enfrente seu primeiro rival Gary ')
    gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
    player.batalhar(gary)
    salvar_jogo(player)

if __name__ == '__main__':
    print('Bem vindo ao game Pokemon de terminal')

    player = carregar_jogo()

    if not player:
        inicio_jogo()

    while True:
        print('\n>>> O que deseja fazer? ')
        print('1 - Explorar o mundo ')
        print('2 - Lutar com um inimigo ')
        print('3 - Ver Pokeagenda ')
        print('4 - Comecar novo jogo ')
        print('0 - Sair do jogo ')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        elif escolha == '4':
            inicio_jogo()
        else:
            print('>>> opcao invalida')

