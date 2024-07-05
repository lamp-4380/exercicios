i = [0]
q = 11
while len(i) < q:
    t = int(input("Digite um número inteiro: "))
    i.append(t)
if (len(i) == q):
    print(sum(i)/(len(i) - 1))