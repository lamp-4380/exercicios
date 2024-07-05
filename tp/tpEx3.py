t = (3,6,2,9,1,7,5,4,14,10)
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(sum(r))