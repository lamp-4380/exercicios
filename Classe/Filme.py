class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    
    def play(self):
        print("Iniciando filme...")
    
class Ação(Filme):
    def __init__(self, nome, duracao,poderes,vilão):
        super().__init__(nome, duracao)
        
        self.poderes = poderes
        self.vilão = vilão
    
    def Explodir(self):
        print("BOOOM")

class Terror(Filme):
    def __init__(self, nome, duracao,personagens,monstro):
        super().__init__(nome, duracao,)
        self.per = personagens
        self.monstro = monstro
    
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
