def trab(sal,h,hex):
    ht = h + hex
    if ht <= 40:
        salt = sal * h
    if ht > 40:
        salt = (sal * h) + (sal/2)*hex
    return salt

print(trab(100,40,2))