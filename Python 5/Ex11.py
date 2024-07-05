def cal(a,b,s):
    if s == "/":
        res = a / b
        return res
    if s == "*":
        res = a * b
        return res
    if s == "+":
        res = a + b
        return res
    if s == "-":
        res = a - b
        return res
    
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
s = input("Digite um sinal de operação(+,-,*,/): ")
print(cal(a,b,s))