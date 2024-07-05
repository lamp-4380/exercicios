x = float(input("Escreva qual sua nota na primeira prova: "))
y = float(input("Escreva qual sua nota na segunda prova: "))
z = float(input("Escreva qual sua nota na terceira prova: "))

nf = ((x + y)/4 + (z)/2)
nfv = nf*10
if(nfv >= 60):
    print("você passou na prova! Sua média ficou ", nf)
else:
    print("Você está reprovado ou de recuperação, pois sua média ficou ", nf)