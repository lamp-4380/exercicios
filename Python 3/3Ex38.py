n = float(input("Escreva um número: "))
d = []
p = []
c = 1
while len(p) < n:
    for i in range(1,c+1):
        if c % i == 0:
            d.append(c)
    if len(d) == 2:
        p.append(c)
    c += 1
    d = []
print(p)
print(sum(p))