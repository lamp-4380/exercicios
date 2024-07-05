l1 = []
n1 = int(input("Digite um número: "))
for i in range(1,n1):
    if n1 % i == 0:
        l1.append(i)
print("A soma dos divisores desse número é ",sum(l1))