class Aluno:
    def __init__(self,nome,ra,n1,n2,n3,n4):
        self.nome = nome
        self.ra = ra
        self.med = (n1+n2+n3+n4)/4
    
    def Mostrar_situacao(self):
        if self.med >= 7:
            print("Aprovado")
        if 5 <= self.med <= 6.9:
            print("Exame")
        if self.med < 5:
            print("Reprovado")

k = Aluno("Kaiser",741539,10,10,10,10)
k.Mostrar_situacao()