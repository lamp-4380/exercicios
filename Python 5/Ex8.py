def CemF(C):
    F = C * (9 / 5) + 32
    return print(f"Essa temperatura em farenheit fica {F:.2f}")

c = int(input("Digite uma temperatura em °C: "))
CemF(c)