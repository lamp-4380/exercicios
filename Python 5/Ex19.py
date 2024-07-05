from random import randint
l = []
def sorteia(x,y):
    
    for i in range(5):
        l.append(randint(x,y))
    return l

x = int(input("Digite o menor número do sorteio: "))
y = int(input("Digite o maior número do sorteio: "))
print(sorteia(x,y))
def somapar():
    l2 = []
    for i in l:
        if i % 2 == 0:
            l2.append(i)
            print(l2)
    return sum(l2)

print(somapar())