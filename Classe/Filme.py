class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    
    def play(self):
        print("Iniciando filme...")
    
class Ação(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    def __init_subclass__(cls,poderes,vilão):
        cls.poderes = poderes
        cls.vilão = vilão
        return super().__init_subclass__()
    
    def Explodir(self):
        print("BOOOM")

class Terror(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    def __init_subclass__(cls,personagens,monstro):
        cls.per = personagens
        cls.monstro = monstro
        return super().__init_subclass__()
    
    def Aparicao(self):
        print("AAAAHHHHH")

class Anphitruo:
    def __init__(self,energia,jogos,jogadores):
        self.energia = energia
        self.jogos = jogos
        self.jogadores = jogadores
    
    def comecaJogos(self):
        print("VAMOS COMEÇAR OS JOGOS AHAHAHAHAHAHHA")
    
    def trocarMascara(self):
        print("A MÁSCARA AGORA É DO 4NFITRI40")
        print("4H4H4H4H4H4H4H4H")
