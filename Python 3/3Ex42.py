n = 1
while n > 0:
    q = n**2
    c = n **3
    r = n **0.5
    print(q)
    print(c)
    print(r)
    n = int(input("Escreva um número natural(inválido para encerrar): "))
if n < 0:
    print("FIM")