class Imóvel:
    def __init__(self,ins_mun,val_aluguel,iptu,piscina,churrasqueira,área,elevador,quartos,area_lazer):
        self.ins = ins_mun
        self.val = val_aluguel
        self.iptu = iptu
        self.piscina = piscina
        self.churras = churrasqueira
        self.area = área
        self.elev = elevador
        self.quart = quartos
        self.arlaz = area_lazer
    
    def getIPTU(self):
        print(f"O valor do iptu é {self.iptu}")
    
    def setAluguel(self,na):
        self.val = na
class Casa(Imóvel):
    def __init__(self, ins_mun, val_aluguel, iptu, piscina, churrasqueira, área, quartos, area_lazer):
        super().__init__(ins_mun, val_aluguel, iptu, piscina, churrasqueira, área, quartos, area_lazer)
    def __init_subclass__(cls):
        return super().__init_subclass__()
    def Descrever(self):
        print(f"Essa casa tem {self.area}m²")
class Condomínio(Imóvel):
    def __init__(self, ins_mun, val_aluguel, iptu, piscina, churrasqueira, área, quartos, area_lazer):
        super().__init__(ins_mun, val_aluguel, iptu, piscina, churrasqueira, área, quartos, area_lazer)
    def __init_subclass__(cls):
        return super().__init_subclass__()
    def Descrever(self):
        print(f"Esse condomínio tem {self.area}m²")
class Apartamento(Imóvel):
    def __init__(self, ins_mun, val_aluguel, iptu, churrasqueira, área, quartos,elevador, area_lazer):
        super().__init__(ins_mun, val_aluguel, iptu, churrasqueira, área, elevador, quartos, area_lazer)
    def __init_subclass__(cls):
        return super().__init_subclass__()
    def Descrever(self):
        print(f"Esse apartamento tem {self.area}m²")
class Terreno(Imóvel):
    def __init__(self, ins_mun, val_aluguel, iptu, área):
        super().__init__(ins_mun, val_aluguel, iptu, área)
    def __init_subclass__(cls):
        return super().__init_subclass__()
    def Descrever(self):
        print(f"Esse terreno tem {self.area}m²")
class Chácara(Imóvel):
    def __init__(self, ins_mun, val_aluguel, iptu, piscina, churrasqueira, área, quartos, area_lazer):
        super().__init__(ins_mun, val_aluguel, iptu, piscina, churrasqueira, área, quartos, area_lazer)
    def __init_subclass__(cls):
        return super().__init_subclass__()
    def Descrever(self):
        print(f"Essa chácara tem {self.area}m²")