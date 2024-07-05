cf = float(input("Escreva a quantidade do custo de fábrica do veículo: "))

if(cf <= 12000):
    ct = cf + (cf * 0.05)
    print("O custo total do veículo é R$ ", ct)
elif(12000 < cf <= 25000):
    ct = cf + (cf * 0.1) + (cf * 0.15)
    print("O custo total do veículo é R$ ", ct)
elif(cf > 25000):
    ct = cf + (cf * 0.1) + (cf * 0.15)
    print("O custo total do veículo é R$ ", ct)
else:
    print("Valor inválido!")