loan = eval(input("請輸入貸款金額: "))
year = eval(input("請輸入貸款年限: "))
rate = eval(input("請輸入念利率: "))
monthrate = rate / (12 * 100) #月利率 百分比

molecules = loan * monthrate
denominator = 1-(1 / (1 + monthrate) ** (year *12))
monthlyPay = molecules / denominator #每月還款金額
totalPay = monthlyPay * year *12 #總還款金額
print(f"每月還款金額 {int(monthlyPay)}")
print(f"總共還款金額 {int(totalPay)}")