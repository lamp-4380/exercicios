a = 0
m = []
mp = []
while a < 10:
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    med = (n1 + n2 + n3 + n4) / 4
    m.append(med)
    a += 1
for i in m:
    if i >= 7:
        mp.append(i)
print(mp)