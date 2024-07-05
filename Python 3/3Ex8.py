i = [0]
q = 11
while len(i) < q:
    t = int(input("Digite um número inteiro: "))
    if t > 0:
         i.append(t)
    else:
        print("Tente novamente")
if (len(i) == q):

    print(sum(i)/(len(i) - 1))