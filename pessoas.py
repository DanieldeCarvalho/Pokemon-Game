class Pessoa:
    def __init__(self, nome=None, pokemons=[]):  # pokemon igual a lista
        if nome:
            self.nome = nome
        else:
            self.nome = 'Anônimo'

        self.pokemons = pokemons


class Player(Pessoa):
    tipo = 'Player'


class Inimigo(Pessoa):
    tipo = 'Inimigo'


eu = Player(nome='Daniel')

print