b = int(input("Digite o valor da base: "))
e = int(input("Digite o valor do expoente: "))
f = 1
for i in range(1,e+1):
    f = f * b
print(f)