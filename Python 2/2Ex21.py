x = float(input("Escreva qual sua nota na primeira prova: "))
y = float(input("Escreva qual sua nota na segunda prova: "))
z = float(input("Escreva qual sua nota na terceira prova: "))

nf = ((x*0.2)+(y*0.3) + (z*0.5))

if(0<=nf<=2.9):
    print("Você passou na prova! Sua média ficou ", nf)
elif(3<=nf<=5.9):
    print("Você passou na prova! Sua média ficou ", nf)


elif(nf>=6):
    print("Você passou na prova! Sua média ficou ", nf)
else:
    print("Valor inválido!")