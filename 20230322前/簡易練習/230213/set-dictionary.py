# s1={3,4,5}
# s2={4,5,6,7}
# # s3 = s1 | s2 #聯集 取不重複所有資料 {3,4,5,6,7}
# # s3 = s1 & s2 #交集 取相同資料{4,5}
# # s3 = s1 - s2 #差集 從s1中減去和s2重複的資料{3}
# # s3 = s1 ^ s2 #反交集 兩個集合中 不重複的資料 {3,6,7}
# print(s3)

# s = set("okhello") 
# print("H" in s)

# dic={"apple":"蘋果","banana":"香蕉"}
# dic["apple"] = "小蘋果"
# print(dic["banana"])

# dic={"apple":"蘋果","banana":"香蕉"}
# print("test" not in dic) #判斷 key是否存在

# dic={"apple":"蘋果","banana":"香蕉"}
# print(dic)
# del dic["apple"] #刪除字典中的建值(key-value pair)
# print(dic)

dic = {x:x*2 for x in [3,4,5]}
print(dic)  #{3: 6, 4: 8, 5: 10}