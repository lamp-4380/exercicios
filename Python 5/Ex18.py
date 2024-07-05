def tri(n):
    h = 2*n-1
    a = ""
    for i in range(0,h+1):
        a += "*"
        print(a)
        if len(a) == n:
            break
    for e in range(n-1,0,-1):
        b = a[:e]
        print(b)
        


n = int(input("Escreva um número: "))

tri(n)