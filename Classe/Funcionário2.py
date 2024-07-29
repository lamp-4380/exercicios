class Funcionario:
    def __init__(self,nome,mat,sal):
        self.nome = nome
        self.matricula = mat
        self.salario = sal
    
    def Bater_ponto(self,umzero=False):
        self.ponto = umzero
        if self.ponto == True:
            print("ponto batido!")
            self.ponto = False

class Vendedor(Funcionario):
    def __init__(self, nome, mat, sal, comm):
        super().__init__(nome, mat, sal)
        self.comm_val = comm

    def Bater_meta(self,meta):
        print(f"Você até agora conseguiu {self.comm_val}/{meta}!")

class Gerente(Funcionario):
    def __init__(self, nome, mat, sal, senha):
        super().__init__(nome, mat, sal)
        self.senha = senha

    def Gerenciar(self):
        print("Gerenciado.")