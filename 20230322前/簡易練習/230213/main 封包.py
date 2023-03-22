#主程式
import geometry.point
result = geometry.point.distance(3,4)
print(result)

import geometry.line as line #建立別名 但下方就都要使用別名
result = line.slope(1,1,2,2)
print("斜率" , result)