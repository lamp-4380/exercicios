t = input("Escreva em que turno você estuda(use M para matutino, V para vespertino e N para noturno): ")
if(t == "M" or t == "m"):
    print("Bom dia!")
elif(t == "V" or t == "v"):
    print("Boa Tarde!")
elif(t == "N" or t == "n"):
    print("Boa Noite!")
else:
    print("Valor inválido!")