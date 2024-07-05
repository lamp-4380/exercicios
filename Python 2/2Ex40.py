t = float(input("Digite o número de horas trabalhadas nesse mês: "))
s = float(input("Digite quanto você recebe por hora: "))
sb = s * t
inss = sb * 0.08
ir = sb * 0.11
sd = sb * 0.05
sl = sb - inss - ir - sd
print("Seu salário bruto, INSS, Imposto de Renda, imposto do Sindicato e salário líquido foi, respectivamente, ", sb,", ",inss,", ",ir,", ", sd," e ", sl)