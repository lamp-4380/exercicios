p = i = 0

while True:
    n = int(input("Escreva um número (0 para encerrar): "))
    if n == 0:
        break
    elif n % 2 == 0:
        p = p + 1
    elif n % 2 != 0:
        i = i + 1
print("Dos números digitados, ", p," eram pares e ", i ," eram ímpares.")