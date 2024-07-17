class Funcionario:
    def __init__(self,nome,sobrenome,ht,vh):
        self.nome = nome
        self.snome = sobrenome
        self.horastrab = ht
        self.valorhora = vh
        self.sal = vh * ht
    def Info(self):
        print(f"Nome Completo: {self.nome} {self.snome}")
        print(f"Salário: {self.sal}")
    
    def IncrementarHoras(self,add):
        self.horastrab += add