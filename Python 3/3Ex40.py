n1 = float(input("Escreva o primeiro número: "))
n2 = float(input("Escreva o segundo número: "))
l1 = []
l2 = []
o = 0
m = 1
if n1 >= n2:
    for i in range(int(n2),int(n1) + 1):
        r = i % 2
        if r == 0:
            l1.append(i)
        elif r != 0:
            l2.append(i)
if n1 <= n2:
    print("Intervalo inválido.")
print(l2)
print(sum(l2))