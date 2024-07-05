v = float(input("Digite o valor do produto: "))

if(v <= 50):
    nv = v + (v*0.05)
    print("O novo valor do produto é ", nv)
if(100 >= v > 50):
    nv = v + (v*0.1)
    print("O novo valor do produto é ", nv)
if(v > 100):
    nv = v + (v*0.15)
    print("O novo valor do produto é ", nv)