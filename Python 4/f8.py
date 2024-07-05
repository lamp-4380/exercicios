def tm(pm,qp):
    ex = (pm*qp) - 50
    if ex == 0:
        return print("Esse é exatamente o limite de quilos!")
    elif ex > 0:
        return print("você excedeu o limite de quilos por", ex,"kg.\
              \nlogo, pagará", ex * 4," reais de multa.")
    elif ex < 0:
        return print("Essa quantidade de peixes está abaixo do limite.")

print(tm(10,6))