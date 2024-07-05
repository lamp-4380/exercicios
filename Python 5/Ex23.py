from random import randint
def alun(qt):
    al = []
    for i in range(qt):
        n = input(f"Digite o nome do aluno {i+1}: ")
        al.append(n)
    a = randint(0,len(al))
    return print(al[a])
qt = int(input("Digite quantos alunos apresentarão a prova: "))
alun(qt)