li = []
i = 1
while i != 0:
    i = int(input("Escreva uma idade(0 para finalizar): "))
    if i != 0:
        li.append(i)
    else:
        break
print(sum(li)/len(li))