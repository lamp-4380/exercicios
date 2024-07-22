class Pessoa:
    def __init__(self,nome,tel,email,endereço):
        self.nome = nome
        self.telefone = tel
        self.email = email
        self.end = endereço
    
    def negociar(self):
        print("Temos um acordo?")
    
class Física(Pessoa):
    def __init__(self, nome, tel, email, endereço):
        super().__init__(nome, tel, email, endereço)
    def __init_subclass__(cls,cpf):
        cls.cpf = cpf
        return super().__init_subclass__()
    def Falar(cls):
        print("bla bla bla")
    
class Jurídica(Pessoa):
    def __init__(self, nome, tel, email, endereço):
        super().__init__(nome, tel, email, endereço)
    def __init_subclass__(cls,cnpj):
        cls.cnpj = cnpj
        return super().__init_subclass__()
    def Dono(cls,ndono):
        print(f"O dono é o(a) {ndono}")