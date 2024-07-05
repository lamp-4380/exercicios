m = [[1, 2,11,13],
     [4,15,16,60],
     [7,8,19,200],
     [20,100,5,3]]
lin = 0
col = 0
a = 3
for i in m:

    for e in i:
        if e > a:
            a = e
            col = i.index(e)
            lin = m.index(i)
        
print("linha",lin+1,"coluna", col+1)