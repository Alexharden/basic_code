a = 0
for i in (range(1,201)):
    a = a+i
print(a)

starting = 1
ending =200
d = 1
sum = int((starting + ending) *(ending - starting +1) /2) #等差數列的公式
print(f"{starting} 到 {ending} 總和是 {sum}")