# 輸入要產生幾層的巴斯卡三角形
n = int(input("請輸入: "))

# 初始化巴斯卡三角形第一層
triangle = [[1]]

# 產生巴斯卡三角形
for i in range(1, n):
    row = [1]  # 初始化每層的第一個元素為 1
    for j in range(1, i):
        # 計算每層中間的元素
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)  # 初始化每層的最後一個元素為 1
    triangle.append(row)  # 將整個層加入巴斯卡三角形列表中

# 輸出巴斯卡三角形
for row in triangle:
    num_str_list = []  # 初始化儲存每個數字字串的列表
    for num in row:
        num_str_list.append(str(num))  # 將每個數字轉為字串後加入列表
    row_str = " ".join(num_str_list)  # 將整個層的數字字串合併為一個字串
    print(row_str)  # 輸出整個層的數字字串
