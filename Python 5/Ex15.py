def linha(qt):
    igual = ""
    for i in range(0,qt):
        igual += "="
    return print(igual)
qt = int(input("Digite quantas linhas serão imprimidas: "))
linha(qt)