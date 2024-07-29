class Passagem:
    def __init__(self,preço,assento):
        self.pre = preço
        self.assento = assento
    
    def alterar_preço(self,np):
        self.pre = np
    
    def escolher_assento(self,na):
        self.assento = na

class PassagemBus(Passagem):
    def __init__(self, preço, assento,placa,leito):
        super().__init__(preço, assento)
        self.placa = placa
        self.leito = leito
    
    def Abastecer(self):
        print("Abastecendo")

class PassagemAviao(Passagem):
    def __init__(self, preço, assento,portemb,checkin):
        super().__init__(preço, assento)
        self.portemb = portemb
        self.checkin = checkin
    
    def decolar(self):
        print("Decolando!")