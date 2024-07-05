def matr(ls):
    mat = [[10,20,30,40],
           [45,26,33,78],
           [19,18,17,16],
           [13,14,15,16]]
    l =[]
    for i in range(0,4):
        l.append(mat[ls][i])
    
    return sum(l)

print(matr(2))