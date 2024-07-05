v = float(input("Escreva o valor de aquisição do produto: "))
if(v >= 50.00):
    vt = v + (v*0.3)
    print("O valor total de venda é: ", vt)
else:
    vm = v + (v*0.45)
    print("O valor total de venda é: ", vm)