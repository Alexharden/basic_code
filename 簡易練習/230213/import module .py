#載入內建的 sys 模組 並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

#建立 自訂模組 名稱 geometry 
# import geometry
# result = geometry.distance(1,1,4,4)
# print(result)
# result = geometry.slope(1,3,5,7)
# print(result)

#調整搜尋模組的路徑
import sys
sys.path.append("modules 模組") # 模組搜尋路徑列表中[新增路徑]
print(sys.path) #印出 模組的搜尋路徑列表
import geometry
print(geometry.distance(10,20,30,40))