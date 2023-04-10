# sum = 0
# for i in range(1, 101, 2):
#     sum += i
# print("1到100之间所有奇数的和为：", sum)

sum = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum += i
print("1到100之间所有奇数的和为：", sum)
