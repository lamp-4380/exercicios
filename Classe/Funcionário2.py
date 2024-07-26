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
    def __init__(self, nome, mat, sal):
        super().__init__(nome, mat, sal)
    
    def __init_subclass__(cls,comm):
        cls.comm_val = comm

        return super().__init_subclass__()
    def Bater_meta(cls,meta):
        print(f"Você até agora conseguiu {cls.comm_val}/{meta}!")

class Gerente(Funcionario):
    def __init__(self, nome, mat, sal):
        super().__init__(nome, mat, sal)
    def __init_subclass__(cls,senha):
        cls.senha = senha
        return super().__init_subclass__()
    def Gerenciar(cls):
        print("Gerenciado.")