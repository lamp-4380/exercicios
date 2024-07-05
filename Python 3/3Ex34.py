n2 = float(20)
l0 = []
l1 = []
l2 = []
o = 0
m = 1
while n2 > 0:
    n1 = float(input("Escreva um número: "))
    l0.append(n1)
    r = n1 % 2
    if r == 0:
        l1.append(n1)
    elif r != 0:
        l2.append(n1)
    n2 -= 1
print(l1)
print(l2)