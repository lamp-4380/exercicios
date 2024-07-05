p = int(input("Digite o código do pedido: "))
q = int(input("Digite quantas unidades do pedido você quer: "))

if(p == 100):
    v = 12*q
    print("Isso vai dar ", v," reais")
elif(p == 102):
    v = 18.5*q
    print("Isso vai dar ", v," reais")
elif(p == 103):
    v = 25.5*q
    print("Isso vai dar ", v," reais")
elif(p == 104):
    v = 17*q
    print("Isso vai dar ", v," reais")
elif(p == 105):
    v = 9.5*q
    print("Isso vai dar ", v," reais")
elif(p == 106):
    v = 6*q
    print("Isso vai dar ", v," reais")
else:
    print("Código inválido!")