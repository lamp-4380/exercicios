class Gato:
    def __init__(self,nome,cor,idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
    
    def hello(self):
        print(f"{self.nome}: Miau")


gato1 = Gato("Gato de botas","laranja", 5)
gato2 = Gato("Ragnar", "Preto e verde", 12)

gato1.hello()
gato2.hello()

print(gato1.cor)
print(gato2.cor)