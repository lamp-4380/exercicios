c = float(input("Escreva o algarismo da centena: "))
d = float(input("Escreva o algarismo da dezena: "))
u = float(input("Escreva o algarismo da unidade: "))

r = c + d + u
if(c >= 0 and d >= 0 and u >= 0):
    print("A soma dos algarismos é ", r)
else:
    print("Um dos números é negativo!")