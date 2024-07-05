na = int(input("Escreva o número de avaliações feitas: "))
ln = []
cont = 0
while cont < na:
    cont += 1
    n = float(input("Digite o valor da avaliação %d : "%(cont)))
    ln.append(n)
print("Sua média nessa matéria é: ",sum(ln)/na)