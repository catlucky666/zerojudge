n = int(input())
x0, y0 = 0, 0  # 起始位置
a, b, c = 0, 0, 0  # 左转、右转、迴转计数

# 读取第一个目标点
x1, y1 = map(int, input().split())

# 计算从 (0, 0) 到 (x1, y1) 的转向
if x1 > x0:  # 从 (0, 0) 向右移动
    last_direction = 0  # 0: 右, 1: 上, 2: 左, 3: 下
elif y1 > y0:  # 从 (0, 0) 向上移动
    last_direction = 1
elif x1 < x0:  # 从 (0, 0) 向左移动
    last_direction = 2
else:  # 从 (0, 0) 向下移动
    last_direction = 3

# 更新坐标
x0, y0 = x1, y1

# 读取后续点并计算转向
for _ in range(1, n):
    x1, y1 = map(int, input().split())
    
    # 判断新的方向
    if x1 > x0:
        new_direction = 0  # 右
    elif y1 > y0:
        new_direction = 1  # 上
    elif x1 < x0:
        new_direction = 2  # 左
    else:
        new_direction = 3  # 下

    # 根据方向判断转向
    if (last_direction + 1) % 4 == new_direction:  # 左转
        a += 1
    elif (last_direction + 3) % 4 == new_direction:  # 右转
        b += 1
    elif (last_direction + 2) % 4 == new_direction:  # 迴转
        c += 1

    # 更新坐标和方向
    x0, y0 = x1, y1
    last_direction = new_direction

# 输出左转、右转、迴转的次数
print(a, b, c)
