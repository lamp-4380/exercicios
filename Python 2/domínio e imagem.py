i = 0
vet1 = []
vet2 = []
while i < 5:
    n1 = float(input("Escreva um número para a posição %d : " %(i)))
    vet1.append(n1)
    n2 = n1 * 5
    vet2.append(n2)
    i = i + 1
print(vet1)
print(vet2)