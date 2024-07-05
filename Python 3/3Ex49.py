li = []
i = 1
p = []
while i != 0:
    i = int(input("Escreva um número(0 para finalizar): "))
    if i != 0:
        li.append(i)
        if i % 2 == 0:
            p.append(i)
    else:
        break
print(sum(li))
print(len(li))
print(sum(li)/len(li))
print(max(li))
print(min(li))
print(sum(p)/len(p))