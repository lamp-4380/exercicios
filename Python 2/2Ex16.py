v = float(input("Escreva o número de horas trabalhadas em um mês: "))
v1 = v * 40.5
if(v1 >= 2500):
    vf = v1 - (v1*0.11)
    print("O valor total é: ", vf)
else:
    vf = v1
    print("O valor total é: ", vf)