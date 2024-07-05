a = [("João",8.0),("Pedro",7.5),("Maria",9.5),("Ana",8.5)]
n = []

for i in a:
    n.append(i[1])
mnl = n.index(max(n))
mn = a[mnl]
print(f"{mn[0]}, {mn[1]}")