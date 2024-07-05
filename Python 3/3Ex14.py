n = int(input("Escreva um número inteiro par: "))
r = 0
i = []
if n % 2 == 0:
    while r < n:
        i.append(r)
        r = r + 2
    if r == n:
        i.append(n)
        print(i)
else:
    print("Esse número não é par")