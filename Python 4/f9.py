def calcularTempo(t):
    val = 9
    if t < 15:
        return 0
    if 16<t<=60:
        th = 1
        return val
    if t > 60:
        th = round(t/60,1)
        for i in range(int(th)-1):
            val +=1.5
        return val
    
print(calcularTempo(120))