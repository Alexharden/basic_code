def generate_triangle(n):
    """
    生成帕斯卡三角形的函數。

    參數：
    n -- 生成三角形的行數

    回傳：
    帕斯卡三角形，以二維串列的形式儲存。

    範例：
    generate_triangle(5)
    回傳：
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    """
    # 初始化三角形的第一行
    triangle = [[1]]
    # 生成後面幾行
    for i in range(1, n):
        # 初始化一行的第一個元素
        row = [1]
        # 生成一行中間的元素
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # 初始化一行的最後一個元素
        row.append(1)
        # 把一行加到三角形的串列中
        triangle.append(row)
    # 回傳生成的帕斯卡三角形
    return triangle

# 測試 generate_triangle 函數
n = int(input("請輸入: "))
triangle = generate_triangle(n)
for row in triangle:
    num_str_list = []
    for num in row:
        num_str_list.append(str(num))
    row_str = " ".join(num_str_list)
    print(row_str)
