p = float(input("Escreva seu peso: "))
h = float(input("Escreva sua altura: "))
imc = (p / h) * 2
if(imc <= 18.5):
    print("Você está abaixo do peso")
elif(24.9 >= imc >= 18.6):
    print("Você está saudável")
elif(25 <= imc <= 29.9):
    print("Você possui peso em excesso")
elif(30 <= imc <= 34.9):
    print("Você está com obesidade grau 1")
elif(35 <= imc <= 39.9):
    print("Você está com obesidade grau 2")
elif(imc >= 40):
    print("Você está com obesidade grau 3")
