import random

n = random.randint(1,100)
c = 0
while c != n:
    c = int(input("Chute um número: "))
    if c > n:
        print("O número chutado é maior que a resposta")
    elif c < n:
        print("O número chutado é menor que a resposta")
if c == n:
    print("Parabéns, você acertou!")