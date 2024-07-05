l = []
n = int(input("Escreva um número inteiro positivo: "))
r = 1
if n > 0:
    while len(l) < n:
        l.append(r)
        r = r + 1
    if len(l) == n:
        print(sum(l))
else:
    print("Número Inválido.")
