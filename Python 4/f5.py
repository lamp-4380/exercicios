def SomaImposto(taxaImposto,custo):
    total = custo + (custo * taxaImposto)
    return total

print(SomaImposto(0.05,100))