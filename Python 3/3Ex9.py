i = []
q = 10
while len(i) < q:
    t = float(input("Digite um número: "))
    i.append(t)
if (len(i) == q):
    print(max(i))
    print(min(i))