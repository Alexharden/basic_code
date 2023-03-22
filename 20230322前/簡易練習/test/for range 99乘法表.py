
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        #<3d 是排版
        print(f"{i}*{j}={result:<3d}", end=" ") #value * value = result ,end=" " 空格
    print()  #換行