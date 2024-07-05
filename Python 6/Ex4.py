try:
    g = input("Digite seu gênero(M para masculino, F para feminino e L para LGBT): ")
    if g != "M" or g != "m" or g != "F" or g != "f" or g != "L" or g != "l":
        raise AttributeError
    else:
        print("Agradecemos pela compreensão.")
except AttributeError:
    print("Valor inválido")