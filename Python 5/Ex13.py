def exp(x,z):
    ex = x
    for i in range(1,z):
        x *= ex
    return x

x = int(input("Digite um número:"))
z = int(input("Digite outro número:"))
print("A potência de",x,"elevado a",z,"é igual a", exp(x,z))