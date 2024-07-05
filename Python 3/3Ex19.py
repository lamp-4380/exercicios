n = input("Escreva um número entre 100 e 9999: ")
r = int(n)
if 100 < r < 9999:
    for i in n:
        print(i)
else:
    print("Número inválido")