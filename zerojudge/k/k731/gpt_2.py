n = int(input())
x0, y0 = 0, 0
a, b, c = 0, 0, 0
x1, y1 = map(int, input().split())
if x1 > x0:
    last_direction = 0 
elif y1 > y0:
    last_direction = 1
elif x1 < x0:
    last_direction = 2
else:  # 从 (0, 0) 向下移动
    last_direction = 3
# 更新坐标
x0, y0 = x1, y1
for _ in range(1, n):
    x1, y1 = map(int, input().split())
    if x1 > x0:
        new_direction = 0  # 右
    elif y1 > y0:
        new_direction = 1  # 上
    elif x1 < x0:
        new_direction = 2  # 左
    else:
        new_direction = 3  # 下
    if (last_direction + 1) % 4 == new_direction:  # 左转
        a += 1
    elif (last_direction + 3) % 4 == new_direction:  # 右转
        b += 1
    elif (last_direction + 2) % 4 == new_direction:  # 迴转
        c += 1
    x0, y0 = x1, y1
    last_direction = new_direction
print(a, b, c)