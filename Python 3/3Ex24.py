l1 = []
for i in range(1,1000):
    if i % 3 == 0:
        l1.append(i)
    elif i % 5 == 0:
        l1.append(i)
print(l1)
print(sum(l1))