def distance(x1,y1,x2,y2): #計算兩點的距離
    return ((x2-x1) ** 2 + (y2-y1) ** 2) **0.5 #((x2-x1)^2 + (y2-y1)^2 開根號))
def slope(x1,y1,x2,y2): #計算線段的斜率
    return(y2-y1) / (x2-x1)