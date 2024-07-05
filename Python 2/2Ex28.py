v = input("Digite uma operação(soma de 2 números, subtração de 2 números (maior - menor), multiplicação de 2 números ou divisão de 2 números): ")
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if(v == "soma de 2 números"):
    vf = n1 + n2
    print("O resultado dessa operação é: ", vf)
elif(v == "subtração de 2 números"):
    if(n1 > n2):
        vf = n1 - n2
        print("O resultado dessa operação é: ", vf)
    elif(n1 > n2):
        vf = n2 - n1
        print("O resultado dessa operação é: ", vf)
elif(v == "multiplicação de 2 números"):
    vf = n1 * n2
    print("O resultado dessa operação é: ", vf)
elif(v == "divisão de 2 números"):
    if(n2>0):
        vf = n1 / n2
        print("O resultado dessa operação é: ", vf)
    else:
        print("O divisor não pode ser 0!")
else:
    print("Operação inválida!")