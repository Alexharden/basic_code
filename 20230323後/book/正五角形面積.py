import math
s = eval(input("輸入五角形的邊長: "))
area = (5* s ** 2) / (4* math.tan(math.pi / 5))
print(f"{int(area) } ")
