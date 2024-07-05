n = int(input("Escreva um número: "))
f = 1
print(f"{n}! = ", end='')
for i in range(n,0,-1):
    f *= i
    if i == 1:
        print(i, end= " = ")
    else:
        print(i, end=' * ')

print(f)