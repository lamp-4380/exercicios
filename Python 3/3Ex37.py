n = int(input("Escreva um número: "))
d = []
for i in range(1,n+1):
    if n % i == 0:
        d.append(i)
if len(d) == 2:
    print("Esse número é primo!")
if len(d) != 2:
    print("Esse número não é primo!")