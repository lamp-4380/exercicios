bm = float(input("Escreva o valor da base maior(B>0): "))
b = float(input("Escreva o valor da base menor(b>0): "))
h = float(input("Escreva o valor da altura(h>0): "))

a = ((b + bm)*h)/2
if(bm<=0 or b <=0 or h<=0):
    print("Um dos valores é inválido!")
else:
    print("a área do trapézio é: ", a)