v = float(input("Qual o valor do produto? "))
e = str(input("Qual o estado destino do produto?"))

if(e == "MG" or e == "mg"):
    vf = v - (v*0.07)
    print("O valor final para esse produto é")
if(e == "SP" or e == "sp"):
    vf = v - (v*0.12)
    print("O valor final para esse produto é")
if(e == "RJ" or e == "rj"):
    vf = v - (v*0.15)
    print("O valor final para esse produto é")
if(e == "MS" or e == "ms"):
    vf = v - (v*0.08)
    print("O valor final para esse produto é")