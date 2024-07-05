def temp(h,m,s):
    hs = h * 3600
    ms = m * 60
    st = hs + ms + s
    return print("Tempo total(em segundos):", st)

h = int(input("Digite um tempo em horas:"))
m = int(input("Digite um tempo em minutos:"))
s = int(input("Digite um tempo em segundos:"))
temp(h,m,s)