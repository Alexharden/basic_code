st1 = {'A', 'C', 'E'}
st2 = {'B', 'C', 'A', 'D'}

#交集 and 且 
print(st1 & st2)
print(st1.intersection(st2),"\n")

#聯集 或 or
print(st1 | st2)
print(st1.union(st2),"\n")


#差集 取前者有的 不取重複的
print(st1 - st2)
print(st1.difference(st2))
print(st2 - st1)
print(st2.difference(st1),"\n")


# exclusive or 代表'互斥或 兩個都沒有重複到的
print(st1 ^ st2)
print(st1.symmetric_difference(st2), "\n")


#檢查前者是否是後者的子集 
st3 = {"A", "B", "C"}
st4 = {"A", "B", "C", "D", "E", "F"}
st5 = {"C","E","G"}
print(st3 <= st4)
print(st3.issubset(st4))
print(st5 <= st3)
print(st4 <= st3)
print(st4 <= st5)
print(st5 <= st3)
print(st5 <= st4)