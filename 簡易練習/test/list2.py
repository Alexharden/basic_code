data=[[3,4,5],[6,7,8]]

print(data[0][1]) # 4
print(data[1][0]) # 6
print(data[0]) # [3,4,5]

data[0][0:2]=[5,5,5]
print(data[0]) # [5,5,5,5]
print(data) # [[5,5,5,5],[6,7,8]]