def preco(quant):
    pf = 0
    for i in range(1,quant+1):
        pf+=1.99
        print(i, " R$",round(pf,2))

preco(50)