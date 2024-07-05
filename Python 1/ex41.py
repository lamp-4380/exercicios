valor = float(input("Digite o valor da venda: "))

parc = valor * 0.10
pagvista = valor - parc
parcela = valor/3

comissao_avista = pagvista * 0.05
comissao_aprazo= valor * 0.05
print("Compra com desconto: ", pagvista)
print("parcela: ", parcela)
print("Comissão a vista: ", comissao_avista)
print("Comissão a prazo: ", comissao_aprazo)