def sn(a,b):
    e = 0
    for i in range(a,b):
        e += i
    return print("A soma de todos os números entre", a,"e", b,"é", e)

a = int(input("Digite um número: "))
b = int(input("Digite um número maior que o anterior: "))
sn(a,b)