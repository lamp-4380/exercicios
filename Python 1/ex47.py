qn=float(input("digite a quantidade de horas normais trabalhadas\n"))
qe=float(input("digite a quantidade de horas extras trabalhadas\n"))
qt=qn+qe
sl=qt-(qt*0.11)
print("Seus salários brut e líquido são, respectivamente",qt ," e ",sl)
