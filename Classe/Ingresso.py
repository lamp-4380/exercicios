class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor
    
    def AlterarPreço(self,np):
        self.preco = np
    
    def Mostrar_setor(self):
        print(self.preco)
    
class Ingresso_VIP(Ingresso):
    def __init__(self, preco, setor):
        super().__init__(preco, setor)
    def __init_subclass__(cls,camarote,open_bar,open_food,estacionamento):
        cls.cam = camarote
        cls.bar = open_bar
        cls.opfood = open_food
        cls.est = estacionamento
        return super().__init_subclass__()
    def pegarBebida(self):
        print("Aqui está")
    
    def acessarCamarote(self):
        print("Você agora está no camarote")