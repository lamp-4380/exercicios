n = int(input("Escreva um número inteiro par: "))
r = 0
i = []
if n % 2 == 0:
    while r < n:
        i.append(r)
        r = r + 2
        print(i)
    if r == n:
        i.append(n)
        i.reverse()
        print(i)
else:
    print("Esse número não é par")
