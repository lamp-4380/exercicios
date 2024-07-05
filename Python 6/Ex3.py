try:
    sald = int(input("Digite seu saldo: "))
    sac = int(input("Digite o valor a ser sacado: "))
    nsal = sald - sac
    if nsal < 0:
            raise ArithmeticError
except ArithmeticError:
    print("Saldo insuficiente")