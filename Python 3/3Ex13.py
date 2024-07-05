n = int(input("Escreva um número inteiro: "))
r = n
i = []
while len(i) < n:
    i.append(r)
    r = r - 1

if len(i) == n:
    print(i)