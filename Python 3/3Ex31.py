vi = 4000
vp = 0.015
t = 4
while t > 0:
    vi = vi + (vi * vp)
    vp *= 2
    t-= 1
print(vi)