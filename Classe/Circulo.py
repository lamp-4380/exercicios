class Circulo:
    def __init__(self,r):
        self.raio = r
    
    def valorRaio(self):
        print(self.raio)
    def areacirc(self):
        ac = 3.14*(self.raio**2)
        print(ac)
    def compcirc(self):
        cc = 2*3.14*self.raio
        print(cc)