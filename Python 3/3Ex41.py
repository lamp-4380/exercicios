r1 = int(input("Digite o valor de R1: "))
r2 = int(input("Digite o valor de R2: "))

if r1 != 0 or r2 != 0:
    r = (r1 * r2) / (r1 + r2)
    print("R = ", r)
    r1 = int(input("Digite outro valor para R1: "))
    r2 = int(input("Digite outro valor para R2: "))
print("O valor final de R é igual a ", r,".")