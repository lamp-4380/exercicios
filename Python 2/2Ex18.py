h = str(input("Escreva sua altura: "))
s = str(input("Escreva seu sexo(h para homem e m para mulher): "))
ch = (72.7 * h) - 58
cm = (62.1 * h) - 44.7
if(s == "h"):
    print("Sua altura ideal é: ", ch)
elif(s == "m"):
    print("Sua altura ideal é: ", cm)
else:
    print("Sexo inválido")