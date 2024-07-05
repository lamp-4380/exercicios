km = float(input("Quantos quilômetros foram percorridos? "))
l = float(input("Quantos litros de gasolina foram consumidos? "))

c = km/l

if(c<=8):
    print("Venda o carro!")
if(8<c<=14):
    print("Econômico!")
if(c>14):
    print("Super econômico!")