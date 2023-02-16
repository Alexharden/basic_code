import random

chioce_one = []
last = 6
while last >= 1:
    i = random.randint(1,38)
    if i not in chioce_one:
        last -= 1
        chioce_one.append(i)
chioce_one = sorted(chioce_one)
chioce_two = random.randint(1,8)
print(f"第一選區的六個號碼為：{chioce_one}",end=" ")
print()
# print(f"第一選區的六個號碼為：",end=" ")
# for x in chioce_one:
#     print(x, end=" ")
# print("")
print(f"第二選區的一個號碼為：{chioce_two}")
chioce_one.append(chioce_two)
chioce_one = list(map(str,chioce_one))
chioce_one = (", ".join(chioce_one))
print(chioce_one)