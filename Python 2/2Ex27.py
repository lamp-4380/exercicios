a = float(input("Escreva o primeiro valor do triângulo: "))
b = float(input("Escreva o segundo valor do triângulo: "))
c = float(input("Escreva o terceiro valor do triângulo: "))
if(a < b+c and b < a+c and c< a+b):
    if(a == b == c):
        print("Esse triângulo é equilátero")
    elif(a == b != c or a != b == c or b == a != c):
        print("Esse triângulo é isóceles")
    elif(a!=b!=c):
        print("Esse triângulo é escaleno")
else:
    print("Isso não é um triângulo")