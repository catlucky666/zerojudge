def cross_(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]
def is_opposite_sign(v1 , v2):
    return (v1[0] >= 0 and v2[0] < 0) or (v1[0] < 0 and v2[0] >= 0) or \
           (v1[1] >= 0 and v2[1] < 0) or (v1[1] < 0 and v2[1] >= 0)
n = int(input())
points = []
for _ in range(n):
    x , y = map(int, input().split())
    points.append((x , y))
a = 0  # 左
b = 0  # 右
c = 0  # 迴
current_position = (0, 0)
direction = (1, 0)  # 向右

# 遍歷每個座標點
for i in range(n):
    next_position = points[i]
    vector_to_next = (next_position[0] - current_position[0], next_position[1] - current_position[1])
    
    if i > 0:  # 不計算第一個轉向
        cross = cross_(direction, vector_to_next)
        
        if cross > 0:
            a += 1  # 左轉
        elif cross < 0:
            b += 1  # 右轉
        else:  # cross == 0，檢查是否為迴轉
            if is_opposite_sign(direction, vector_to_next):
                c += 1  # 迴轉
    current_position = next_position
    direction = vector_to_next
print(a, b, c)