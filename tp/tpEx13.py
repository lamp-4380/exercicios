a = [[1,13,3],
     [4,45,67],
     [7,80,9]]


b = [[100,8,7],
     [6,5,4],
     [3,25,10]]
sm = []

for i in range(len(a)):
    ls = []
    for e in range(len(a[i])):
        s = a[i][e] + b[i][e]
        ls.append(s)
    sm.append(ls)

for i in sm:
    print(i)