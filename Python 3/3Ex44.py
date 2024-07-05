import time
r = []
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
while True:
    v = input("Digite uma operação: soma de 2 números(1), subtração de 2 números (2), multiplicação de 2 números(3), divisão de 2 números(4) ou sair (5): ")

    if(v == "1"):
        vf = n1 + n2
        print("O resultado dessa operação é: ", vf)
        time.sleep(0.5)
        r.append(vf)
    elif(v == "2"):
        vf = n1 - n2
        print("O resultado dessa operação é: ", vf)
        time.sleep(0.5)
        r.append(vf)
    elif(v == "3"):
        vf = n1 * n2
        print("O resultado dessa operação é: ", vf)
        time.sleep(0.5)
        r.append(vf)
    elif(v == "4"):
        if(n2>0):
            vf = n1 / n2
            print("O resultado dessa operação é: ", vf)
            time.sleep(0.5)
            r.append(vf)
        else:
            print("O divisor não pode ser 0!")
            print("Retornando...")
            time.sleep(0.5)
    elif v == "5":
        print("Resultados (em ordem): ",r)
        break
    else:
        print("Operação inválida!")