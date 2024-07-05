n1 = int(input("Escreva o primeiro termo: "))
n2 = int(input("Escreva o segundo termo: "))
d1 = n1-n2
d2 = n2-n1
if(n1 > n2):
    print("O primeiro número é maior, a diferença deles é de ", d1," unidades")
elif(n2 > n1):
    print("O segundo deles é maior, a diferença entre eles é de ", d2," unidades")
else:
    print("Os 2 são iguais, a diferença entre eles é 0")