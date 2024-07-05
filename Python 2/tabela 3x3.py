l = 3
c = 3
matriz = []
for i in range(l):
    lin = []
    for s in range(c):
        n = int(input("Digite um valor: "))
        lin.append(n)
    matriz.append(lin)
for i in matriz:
    print(i)