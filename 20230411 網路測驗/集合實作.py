shrimp = {"炸鳳尾蝦":["蝦子","核果","油"], "雲龍炸蝦":["核果", "蝦子", "醬汁", "豆皮","油"]}
lee = set(shrimp['炸鳳尾蝦'])
liu = set(shrimp['雲龍炸蝦'])
print(liu - lee)
print(lee - liu)
print(lee & liu)

lee.add("蘋果")
lee.add("洋蔥")
lee.add("醬汁")
print(lee)

print(lee - liu)
shrimp['炸鳳尾蝦'] = list(lee)
print(shrimp)