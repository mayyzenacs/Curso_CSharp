
class Aranha:
    def __init__(self, tipo, numero_pernas):
        self.tipo = tipo
        self.numero_pernas = numero_pernas

class Aranhas_assassinas:
    def __init__(self, poder, cor, tipo, numero_pernas, mata = True):
        self.poder = poder
        self.cor = cor
        super().__init__()


class Aranha_da_tasmania(Aranhas_assassinas):
    def __init__(self, poder, cor, tipo, numero_pernas, mata = True):
        super().__init__(poder, cor, tipo, numero_pernas, mata=True)

class Aranha_eletrica(Aranhas_assassinas):
    pass

class Aranha_azul(Aranha_da_tasmania, Aranhas_assassinas):
    pass


Aranha_tasmania = Aranha()