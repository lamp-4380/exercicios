class Brinquedo:
    def __init__(self,nome,cor,tamanho,preço):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preço = preço
    def Brincar(self):
        print(f"Brincando com {self.nome}")
class McDonalds(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço,tema):
        super().__init__(nome, cor, tamanho, preço)
        self.tema = tema
    def verTema(self):
        print(f"Nessa época o McDonalds tava vendendo brinquedos do {self.tema}")