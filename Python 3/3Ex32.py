nv = 1
l = []
while nv < 6:
    n = int(input(f"Escreva o {nv}º número: "))
    l.append(n)
    nv += 1
print(sum(l))
for i in l:
    print(i)