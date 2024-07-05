n1 = int(input("Escreva um número: "))
n2 = int(input("Escreva um número maior que o anterior: "))
c = 0

for i in range(n1,n2):
    c += 1
print("Entre ", n1," e ", n2," existem ", c ," números.")