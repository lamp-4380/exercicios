class Compra:
    def __init__(self,num,prod,val,vt=0):
        self.num = num
        self.prod = prod
        self.val = val
        self.vt = vt
    def calTotal(self):
        self.vt = (self.val)+(self.val*0.17)+(self.val*0.05)
        print(f"O valor total é {self.vt}")
    
class Avista(Compra):
    def __init__(self, num, prod, val, vt=0):
        super().__init__(num, prod, val, vt)
        self.des = 0.2
        self.vt -= self.des * vt
    
    def getVal(self):
        print(f"Esse valor à vista fica {self.vt} por causa do desconto de {self.des*100}%")
    
class Parcelado(Compra):
    def __init__(self, num, prod, val, parc,vt=0):
        super().__init__(num, prod, val, parc,vt)
        self.parc = parc
        self.val = val
        self.valparc = self.val / self.parc
    def getValParc(self):
        print(f"Se parcelar em {self.parc} vezes, o valor fica {self.valparc} cada")