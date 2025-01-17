# 讀取矩陣的大小
n, m = map(int, input().split())

# 初始化二維數組
a = [[0] * m for _ in range(n)]

# 填充矩陣
for i in range(n):
    a[i] = list(map(int, input().split()))

# 定義函數來計算特殊位置
def find_special_positions(n, m, matrix):
    special_positions = []

    # 遍歷矩陣的每一個元素
    for i in range(n):
        for j in range(m):
            x = matrix[i][j]
            total_sum = 0

            # 計算曼哈頓距離內的總和
            for a in range(n):
                for b in range(m):
                    if abs(a - i) + abs(b - j) <= x:
                        total_sum += matrix[a][b]

            # 判斷是否為特殊位置
            if total_sum % 10 == x:
                special_positions.append((i, j))

    # 按字典序排序特殊位置
    special_positions.sort()
    
    return special_positions

# 獲取特殊位置
special_positions = find_special_positions(n, m, a)

# 輸出結果
print(len(special_positions))
for pos in special_positions:
    print(pos[0], pos[1])