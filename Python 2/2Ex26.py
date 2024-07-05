a = float(input("Escreva um ano: "))

d1 = a%400
d2 = a%4
d3 = a%100

if(d1 == 0 or d2 == 0 and d3 != 0 ):
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")