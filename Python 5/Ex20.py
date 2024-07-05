def tri2(n):
    a = "*"
    f = n*2-1
    
    b = " "
    cont = 1
    for e in range(n,0,-1):
        print((b*e)+(a*cont)+(b*e))
        cont += 2

tri2(10)