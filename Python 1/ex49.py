lt=float(input("quantidade de latas compradas\n"))
gp=float(input("quantidade de garrafas de 600ml compradas\n"))
gg=float(input("quantidade de garrafas de 2l compradas\n"))
ltt=(lt*350)+(gp*600)+(gg*2000)
ltl=ltt/1000
print("O total comprado em litros de refrigerante foi ",ltl,"l")
