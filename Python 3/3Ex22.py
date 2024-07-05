p = 1
n = []
while 10 >= p >= 0:
    p = int(input("Digite uma nota de 0 a 10(número inválido para terminar): "))
    if p >=0 and p <= 10:
        n.append(p)
    else:
        break

print(sum(n) / len(n))