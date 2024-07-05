
def exc(q):
    a = ""
    for i in range(0,q):
        a += "!"
        print(a)
    return a


q = int(input("Digite quantas exclamações serão digitadas: "))
exc(q)