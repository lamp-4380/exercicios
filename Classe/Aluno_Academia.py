class Aluno_Academia:
    def __init__(self,nome,idade,peso,altura,mens=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.alt = altura
        self.mensalidade = mens
        if self.idade < 18:
            self.menoumai = "Menor de Idade"
            self.mensalidade = mens - (mens*0.2)
        else:
            self.menoumai = "Maior de Idade"
    
    def Calcular_IMC(self):
        print(self.peso/(self.altura**2))
    
    def Obter_valor_mensalidade(self):
        print(self.mensalidade)