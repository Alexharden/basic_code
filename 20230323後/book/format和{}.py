number = 30
name = "哈"
count = 1
print("{}你的第 {} 次物理考試成績是 {}".format(name, count, number))

number = 30
name = "哈"
count = 1
string = "{}你的第 {} 次物理考試成績是 {}"
print(string.format(name, count, number))

number = 30
name = "哈"
count = 1
print("{0}你的第 {1} 次物理考試成績是 {2}".format(name, count, number))

print("{n}你的第 {c} 次物理考試成績是 {s}".format(n="哈", c=1, s=30))

#改良
city = "台北"
country = "台灣"
print(f"{city}是{country}的首都")
