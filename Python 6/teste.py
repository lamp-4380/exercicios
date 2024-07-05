while True:
    try:
        a = int(input("Digite um número: "))
        y = int(input("Digite outro número:"))
        b = a / y
        print(b)

    except ZeroDivisionError:
        print("Divisão por zero não né?")
    except ArithmeticError:
        print("Outro erro aritmético.")
    except ValueError:
        print("Apenas números, por favor.")