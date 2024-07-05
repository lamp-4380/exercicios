v = float(input("Digite o valor das vendas: "))

if(v >= 100000):
    vf = 700 + (v * 0.16)
    print("O valor da comissão é ", vf," reais")
elif(100000>v>80000):
    vf = 650 + (v * 0.14)
    print("O valor da comissão é ", vf," reais")
elif(60000<v<80000):
    vf = 600 + (v * 0.14)
    print("O valor da comissão é ", vf," reais")
elif(60000>v>40000):
    vf = 550 + (v * 0.14)
    print("O valor da comissão é ", vf," reais")
elif(40000>v>20000):
    vf = 500 + (v * 0.14)
    print("O valor da comissão é ", vf," reais")
elif(v<20000):
    vf = 450 + (v * 0.14)
    print("O valor da comissão é ", vf," reais")
else:
    print("Valor indeterminado!")