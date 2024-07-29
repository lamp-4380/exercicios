class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor
    
    def AlterarPreço(self,np):
        self.preco = np
    
    def Mostrar_setor(self):
        print(self.preco)
    
class Ingresso_VIP(Ingresso):
    def __init__(self, preco, setor,camarote,open_bar,open_food,estacionamento):
        super().__init__(preco, setor)
        self.cam = camarote
        self.bar = open_bar
        self.opfood = open_food
        self.est = estacionamento

    def pegarBebida(self):
        print("Aqui está")
    
    def acessarCamarote(self):
        print("Você agora está no camarote")