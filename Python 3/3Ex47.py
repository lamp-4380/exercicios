l = []
l2 = []
for i in range(1,101):
    e = i**2
    l.append(e)

for e in range(1,101):
    l2.append(e)
print(sum(l))
print((sum(l2))**2)