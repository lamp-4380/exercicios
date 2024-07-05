li = []
i = 1
while i != 0:
    i = int(input("Escreva um número(negativo para finalizar): "))
    if i != 0:
        li.append(i)
    else:
        break
print(max(li))
print(min(li))