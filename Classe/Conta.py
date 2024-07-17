class Conta:
    def __init__(self,Nome,cpf,num,sal):
        self.nome = Nome
        self.cpf = cpf
        self.numero = num
        self.saldo = sal
    
    def Depositar(self,dd):
        self.saldo += dd
    
    def Sacar(self,ds):
        if ds <= self.saldo:
            self.saldo -= ds
        else:
            print("Saldo Insuficiente")
    
    def Imprimir_saldo(self):
        print(self.saldo)

a = Conta("Arthur","487.628.538-90",40028922,14000)
a.Imprimir_saldo()