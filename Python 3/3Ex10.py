n = int(input("Escreva um número inteiro: "))
r = 0
i = []
while r < n * 2:
    if r % 2 == 0:
        r = r + 1
        i.append(r)
    else:
        r = r + 2
        i.append(r)
if len(i) >= n:
    i.reverse
    i.remove(max(i))
    print(i)