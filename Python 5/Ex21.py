def mat(l,c):
    matr = []

    for i in range(0,l):
        lin = []
        for e in range(0,c):
            lin.append(1)
        matr.append(lin)
    for f in matr:
        print(f)

mat(3,3)