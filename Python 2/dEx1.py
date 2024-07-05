empresa = {'nome':'', 'unidade':'', 'fone':'', 'e-mail':'', 'cidade': '', 'UF': ''}
unidades = []
emails = []

for i in range(4):
    empresa['nome'] = input("Escreva o nome da empresa: ")
    empresa['unidade'] = input("Escreva a unidade da empresa: ")
    empresa['fone'] = input("Escreva qual o número da empresa: ")
    empresa['e-mail'] = input("Escreva o e-mail da empresa: ")
    empresa['cidade'] = input("Escreva a cidade da empresa: ")
    empresa['UF'] = input("Escreva qual a UF da empresa: ")
    print(empresa)
    unidades.append(empresa['unidade'])
    emails.append(empresa['e-mail'])

for e in range(0,4):
    print(unidades[e], emails[e])