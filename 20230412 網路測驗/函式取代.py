r = 33
def t1(r):
	print(r)
	r = 2
	print(r) # 改完變2
lt = [555] 
def t2(lt):
	print(lt)
	lt = 100
	print(lt)

kk = [444]	#字典或list會被取代
def t3(kk):
	print(kk)
	kk[0] = 100	
	print(kk)
	
t1(r)
print(r,"\n")

t2(lt)
print(lt,"\n")

t3(kk)
print(kk,"\n")
