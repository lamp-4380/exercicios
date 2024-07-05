m = [[1, 2,11,13],
     [4,15,16,60],
     [7,8,19,200],
     [20,100,5,3]]
maior = []
for i in m:
    for e in i:
        if e > 10:
            maior.append(e)
print(len(maior))