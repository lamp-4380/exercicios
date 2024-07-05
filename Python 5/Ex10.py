def nota(a1,a2,a3,l):
    if l == "A":
        ma = (a1 + a2 + a3)/3
        return ma
    elif l == "P":
        mp = (a1*0.5)+(a2*0.3)+(a3*0.2)
        return mp
    

a1 = int(input("Digite uma nota de 0 a 10: "))
a2 = int(input("Digite uma nota de 0 a 10: "))
a3 = int(input("Digite uma nota de 0 a 10: "))
l = input("Digite se quer média aritmética ou média ponderada (A ou P): ")
print(nota(a1,a2,a3,l))