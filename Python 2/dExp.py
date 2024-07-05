pessoa = {'nome':'Thiago Almeida','idade':28, 'cidade':'Campo Grande'}

#print(pessoa['nome'])
#print(pessoa['idade'])
#print(pessoa['cidade'])
for value in pessoa.keys():
    print(pessoa[value])
pessoa['cidade'] = 'New York'
print(pessoa['cidade'])