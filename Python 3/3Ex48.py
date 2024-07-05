l = [1,1,4,21,56,43,76,76,33,4,56,77,55,3,0]
i = []
o = []
n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))
i.append(n1)
i.append(n2)
i.append(n3)
o.append(l.count(n1))
o.append(l.count(n2))
o.append(l.count(n3))

print("Ocorrências:")
for e in range(0,3):
    print(i[e]," - Apareceu ", o[e] ," vez(es)")