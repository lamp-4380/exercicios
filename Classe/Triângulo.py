class Triangulo:
    def __init__(self,l1,l2,l3):
        self.ladoA = l1
        self.ladoB = l2
        self.ladoC = l3
    def CalcularPerimetro(self):
        print(self.ladoA+self.ladoB+self.ladoC)
    
    def getMaiorLado(self):
        print(max(self.ladoA,self.ladoB,self.ladoC))
    
n = Triangulo(15,12,20)
n.getMaiorLado()