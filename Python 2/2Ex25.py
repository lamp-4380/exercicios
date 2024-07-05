v = float(input("Digite um símbolo de operação(+, -, * ou /): "))
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if(v == "+"):
    vf = n1 + n2
    print("O resultado dessa operação é: ", vf)
elif(v == "-"):
    vf = n1 - n2
    print("O resultado dessa operação é: ", vf)
elif(v == "*"):
    vf = n1 * n2
    print("O resultado dessa operação é: ", vf)
elif(v == "/"):
    vf = n1 / n2
    print("O resultado dessa operação é: ", vf)
else:
    print("Operação inválida!")