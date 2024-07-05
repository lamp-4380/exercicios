def poun(n):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    elif n < 0:
        return -1

n = int(input("Digite um número: "))
print(poun(n))