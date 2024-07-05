n1 = float(input("Escreva a primeira nota "))
n2 = float(input("Escreva a segunda nota "))
if(0<=n1<=10):
    nf = (n1 + n2)/2
    print("A sua média é ", nf)
else:
    print("Uma das notas não é válida")