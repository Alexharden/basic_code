#https://ithelp.ithome.com.tw/articles/10241349
new_list = []
for i in range(1,11):
    for j in range(1,11):
        if j % 2 ==0 and i % 2 ==0:
            s = i*j
            new_list.append(f"{i} * {j} = {s}")
print(new_list)


