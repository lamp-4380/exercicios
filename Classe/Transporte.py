class Transporte:
    def __init__(self,capacidade):
        self.cap = capacidade
    

class Aquatico(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)

class Terrestre(Transporte):
    def __init__(self, capacidade, nr):
        super().__init__(capacidade,nr)
        self.num_rodas = nr
    
class Aereo(Transporte):
    def __init__(self, capacidade):
        super().__init__(capacidade)

class Automovel(Terrestre):
    def __init__(self, capacidade, nr,cor,np,placa):
        super().__init__(capacidade, nr,cor,np,placa)
        self.cor = cor
        self.num_portas = np
        self.placa = placa
class Lancha(Aquatico):
    def __init__(self, capacidade,velocidade_max):
        super().__init__(capacidade,)
        self.vmax = velocidade_max
class Navio(Aquatico):
    def __init__(self, capacidade,tamanho,nmotores):
        super().__init__(capacidade,)
        self.tam = tamanho
        self.num_motores = nmotores
class AviaoComercial(Aereo):
    def __init__(self, capacidade,empresa):
        super().__init__(capacidade,empresa)
        self.empresa = empresa
class AviaoMonomotor(Aereo):
    def __init__(self, capacidade, on_off):
        super().__init__(capacidade, on_off)
        self.on_off = on_off