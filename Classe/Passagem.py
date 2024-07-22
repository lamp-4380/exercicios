class Passagem:
    def __init__(self,preço,assento):
        self.pre = preço
        self.assento = assento
    
    def alterar_preço(self,np):
        self.pre = np
    
    def escolher_assento(self,na):
        self.assento = na

class PassagemBus(Passagem):
    def __init__(self, preço, assento):
        super().__init__(preço, assento)
    
    def __init_subclass__(cls,placa,leito):
        cls.placa = placa
        cls.leito = leito
        return super().__init_subclass__()
    
    def Abastecer(self):
        print("Abastecendo")

class PassagemAviao(Passagem):
    def __init__(self, preço, assento):
        super().__init__(preço, assento)
    
    def __init_subclass__(cls,portemb,checkin) -> None:
        cls.portemb = portemb
        cls.checkin = checkin
        return super().__init_subclass__()
    
    def decolar(self):
        print("Decolando!")