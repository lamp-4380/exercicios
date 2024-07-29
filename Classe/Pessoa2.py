class Pessoa:
    def __init__(self,nome,tel,email,endereço):
        self.nome = nome
        self.telefone = tel
        self.email = email
        self.end = endereço
    
    def negociar(self):
        print("Temos um acordo?")
    
class Física(Pessoa):
    def __init__(self, nome, tel, email, endereço,cpf):
        super().__init__(nome, tel, email, endereço,cpf)
        self.cpf = cpf

    def Falar(cls):
        print("bla bla bla")
    
class Jurídica(Pessoa):
    def __init__(self, nome, tel, email, endereço,cnpj):
        super().__init__(nome, tel, email, endereço,cnpj)
        self.cnpj = cnpj

    def Dono(cls,ndono):
        print(f"O dono é o(a) {ndono}")