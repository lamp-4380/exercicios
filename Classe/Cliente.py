class Cliente:
    def __init__(self,nome,idade,fone):
        self._nome = nome
        self.idade = idade
        self.fone = fone
    
    def Comprar(self):
        print(f"{self.__nome} realiza compras")
    
    def getNome(self):
        return self.__nome
    
class ClientePremium(Cliente):
    def __init__(self, nome, idade, fone,vip=None,desconto=28):
        super().__init__(nome, idade, fone)
        self.vip = vip
        self.des = desconto
    
    def Comprar(self):
        print(f"{self._nome} compra muito com {self.des}% de desconto.")

cp = ClientePremium("Arthur",19,40444044)
cp.Comprar()