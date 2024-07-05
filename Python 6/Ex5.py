try:
    x = float(input("Digite um valor: "))
    y = x ** 0.5
    print(y)
except ValueError:
    print("Valor impróprio para raiz quadrada.")