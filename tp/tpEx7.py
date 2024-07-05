m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
l = []

mt = []
for i in m:
    l.append(i[0])
mt.append(l)
l = []
for i in m:
    l.append(i[1])
mt.append(l)
l = []
for i in m:
    l.append(i[2])
mt.append(l)
for i in mt:
    print(i)