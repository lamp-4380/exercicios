i=0
while (i<5):
    print(i)
    i=i+1
    continue


i=6
while(i>0):
    i=i-3
    print(i)
    continue

x=10
while not(x==0):
    x=x-1
    if x%2!=0:
        print(x)
        continue

terminou=False
p=i=0
while(not terminou):
    n=int(input("digite um numero para continuar ou zero para termiar\n"))
    if n==0:
        terminou=True
    else:
        if n%2==0:
            p=p+1
        else:
            i=i+1
    continue
print("p= ",p)
print("i= ",i)


numeros=[2,11,4,11,5,9,99,11]
i=-1
contador=0
print(len(numeros))
while i<len(numeros)-1:
    i=i+1
    if numeros[i]!=11:
        continue    
    else:
        print("11 esta aqui")
        contador+=1
    continue
print("quantidade de numeros 11 encontrados: ",contador)

