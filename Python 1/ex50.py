import math
x1=float(input("digite um valor para x1\n"))
x2=float(input("digite um valor para x2\n"))
y1=float(input("digite um valor para y1\n"))
y2=float(input("digite um valor para y2\n"))
d= math.sqrt((x1 - x2)**2+(y1 - y2)**2)
if d >=10:
 print("LONGE")
else:
 print("PERTO")