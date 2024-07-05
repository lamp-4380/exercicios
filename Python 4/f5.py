#Escreva um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
#que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” 
#o valor de custo para incluir o imposto sobre vendas. Por fim deve retornar o novo valor para o usuário considerando o percentual
#do imposto.
def SomaImposto(taxaImposto,custo):
    total = custo + (custo * taxaImposto)
    return total

print(SomaImposto(0.05,100))