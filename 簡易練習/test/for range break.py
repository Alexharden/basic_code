print("測試1")
for digit in range(1, 11):
    if digit == 5: #條件成立 遇到break 中止此迴圈
        break
    print(digit, end=", ")
print()
print("測試2")
for digit in range (0, 11, 2):
    if digit == 5: #間隔2 所以會跳過 條件成立 不會執行break
        break
    print(digit, end=", ")