def area(r):
    pi = 3.14
    return 3.14 * r ** 2 # 會將計算完的結果輸出到呼叫它的地方

print(f"半徑長為1的圓，其面積為：{area(1)}")
print(f"半徑長為3的圓，其面積為：{area(3)}")



def area1(r, pi=3.14):
    return pi * r ** 2

print(f"半徑長為1的圓，其面積為：{area1(1,3.14159)}") #位置參數
print(f"半徑長為3的圓，其面積為：{area1(3)}")
print(f"半徑長為3的圓，其面積為：{area1(pi=3.141, r = 3)}")



def All(r, pi=3.14):
	def area():
		return pi * r ** 2
	def perimeter():
		return 2 * pi * r
	# 下面{}的用法是所謂的format，可以將多個變數按照順序放置到{}中
	print('半徑 = {}的圓，其周長 = {}，面積 = {}'.format(r, area(), perimeter()))
	print(f"半徑 = {r}的圓，其周長 = {area()}，面積 = {perimeter()}")
All(3, 3.14159)


def All1(r, pi=3.14):
	def area():
		return pi * r ** 2
	def perimeter():
		return 2 * pi * r
	return area(), perimeter()
ans = All1(3, 3.14159)
print(f"半徑 = 3的圓，其周長 = {ans[0]}，面積 = {ans[1]}")
