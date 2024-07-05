i = int(input("Escreva sua idade: "))
t = int(input("Escreva por quantos anos você trabalhou: "))

if(1 >= 65 or t >=30 or (1>=60 and t >=25)):
    print("Você já pode se aposentar!")
else:
    print("Você ainda não pode se aposentar")