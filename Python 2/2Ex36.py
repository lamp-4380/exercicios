s = float(input("Escreva qual o seu salário: "))
t = float(input("Escreva a quanto tempo você trabalha na empresa(anos): "))
if(s<=500):
    sf = s + (s * 0.25)
    print("Seu novo salário é: R$ ", sf)
elif(500<s<=1000):
    sf = s + (s * 0.20)
    print("Seu novo salário é: R$ ", sf)
elif(1000 < s <= 1500):
    sf = s + (s * 0.15)
    print("Seu novo salário é: R$ ", sf)
elif(1500 < s <= 2000):
    sf = s + (s * 0.10)
    print("Seu novo salário é: R$ ", sf)
else:
    sf = s
    print("Seu novo salário é: R$ ", sf ," (não houve reajuste)")
ns = float(print("escreva como ficou seu salário após o aumento: "))
if(t<1):
    vf = ns
    print("Você não recebeu bônus de tempo de trabalho")
if(1<t<3):
    vf = ns + 100
    print("Você recebeu um bônus! Seu novo salário é ", vf," reais")
if(4<t<6):
    vf = ns + 200
    print("Você recebeu um bônus! Seu novo salário é ", vf," reais")
if(7<t<10):
    vf = ns + 300
    print("Você recebeu um bônus! Seu novo salário é ", vf," reais")
if(t > 10):
    vf = ns + 500
    print("Você recebeu um bônus! Seu novo salário é ", vf," reais")