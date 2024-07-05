def calcularTempo(t):
    val = 9
    th = round(t/60,1)
    if t < 15:
        th = 0
    elif t > 16:
        for i in range(int(th)-1):
            val +=1.5
    pis = val*0.033
    cofins = val*0.02
    icms =val*0.17
    vi = pis + cofins + icms
    print(f"Tempo {th:.2f} horas")
    print(f"PIS: R$ {pis:.2f}")
    print(f"COFINS: R$ {cofins:.2f}")
    print(f"ICMS: R$ {icms:.2f}")
    print(f"IMPOSTOS: R$ {vi:.2f} ")
    print(f"TOTAL: R$ {val + vi:.2f}")

calcularTempo(240)