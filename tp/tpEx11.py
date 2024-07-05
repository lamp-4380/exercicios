m = [[1,120,-3],
     [4,5,250],
     [7,0,9]]
lin = 0
col = 0
a = 3
for i in m:

    for e in i:
        if e > a:
            a = e
            col = i.index(e)
            lin = m.index(i)
        
print("Maior: linha",lin+1,"coluna", col+1)
b = 5000
for i in m:

    for e in i:
        if e < a:
            a = e
            col = i.index(e)
            lin = m.index(i)
        
print("Menor: linha",lin+1,"coluna", col+1)