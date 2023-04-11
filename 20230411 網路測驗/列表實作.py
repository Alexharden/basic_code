#https://ithelp.ithome.com.tw/articles/10240088

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lt1 = lt[::2]
lt2 = lt[1::2]

lt1.extend(lt2)
print(lt1)

del lt1[7]
del lt1[1]
print(lt1)
lt1.sort()
print(lt1)