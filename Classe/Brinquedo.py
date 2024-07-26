class Brinquedo:
    def __init__(self,nome,cor,tamanho,preço):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preço = preço
    def Brincar(self):
        print(f"Brincando com {self.nome}")
class McDonalds(Brinquedo):
    def __init__(self, nome, cor, tamanho, preço):
        super().__init__(nome, cor, tamanho, preço)
    def __init_subclass__(cls,tema):
        cls.tema = tema
        return super().__init_subclass__()
    def verTema(cls):
        print(f"Nessa época o McDonalds tava vendendo brinquedos do {cls.tema}")