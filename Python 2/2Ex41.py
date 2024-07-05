eq = str(input("Escreva a equação: "))
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = (b**2) - 4 * a * c
x1 = (-b + (d ** 0.5))/2*a
x2 = (-b - (d ** 0.5))/2*a
if(d<0):
    print("Não existe raiz real")
elif(d==0):
    print("Existe uma raiz real(", x1,")")
if(d>0):
    print("Existem 2 raizes reais (", x1," e ", x2,")")