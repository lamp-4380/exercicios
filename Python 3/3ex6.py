i = [0]
q = 11
while len(i) < q:
    t = float(input("Digite um número: "))
    i.append(t)
if (len(i) == q):
    print(sum(i))