l = []
v = 50
e = 0
while len(l) < v:
    e = e + 2
    l.append(e)
if(len(l) == v):
    print(sum(l))