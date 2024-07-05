ne = int(input("Escreva quantos números deve haver na lista: "))
l = []

while len(l) < ne:
    p = float(input("Escreva um número: "))
    l.append(p)
if len(l) == ne:
    print(max(l))