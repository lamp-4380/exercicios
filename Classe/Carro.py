class Carro:
    def __init__(self, modelo, cor, marca, placa, ano, vmax):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.vmax = vmax
    def MostrarCarro(self):
        print(f"Esse carro é um {self.modelo} {self.cor}, ele é da marca {self\
            .marca}, de {self.ano}, placa {self.placa}.")
    
    def CordoCarro(self):
        print(f"Ele é da cor {self.cor}, que é meio bonita, eu acho...")
    
    def CarroGeral(self):
        print(f"Ele é um {self.modelo} da {self.marca}.")
    
    def Velocidade(self):
        print(f"Ele chega até {self.vmax} Km/h.")
    
    def UnoSimouNao(self):
        if self.modelo == "Uno":
            print("Esse carro aí é top viu?")
        else:
            print("Ah... dá pro gasto né...")

carro = Carro("Uno","Branco","Fiat","XLR-0008","1999","325")

carro.MostrarCarro()
carro.CordoCarro()
carro.CarroGeral()
carro.Velocidade()
carro.UnoSimouNao()