
def cross_product(v1, v2):
    """計算兩個向量的外積"""
    return v1[0] * v2[1] - v1[1] * v2[0]

def is_opposite_sign(v1, v2):
    """檢查兩個向量是否為異號"""
    return (v1[0] >= 0 and v2[0] < 0) or (v1[0] < 0 and v2[0] >= 0) or \
           (v1[1] >= 0 and v2[1] < 0) or (v1[1] < 0 and v2[1] >= 0)

# 讀取輸入
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 計數器
left_turns = 0
right_turns = 0
u_turns = 0

# 初始化起始位置和方向
current_position = (0, 0)
current_direction = (1, 0)  # 初始向右

# 遍歷每個座標點
for i in range(n):
    next_position = points[i]
    vector_to_next = (next_position[0] - current_position[0], next_position[1] - current_position[1])
    
    if i > 0:  # 不計算第一個轉向
        cross = cross_product(current_direction, vector_to_next)
        
        if cross > 0:
            left_turns += 1  # 左轉
        elif cross < 0:
            right_turns += 1  # 右轉
        else:  # cross == 0，檢查是否為迴轉
            if is_opposite_sign(current_direction, vector_to_next):
                u_turns += 1  # 迴轉

    # 更新當前位置和方向
    current_position = next_position
    current_direction = vector_to_next

# 輸出結果
print(left_turns, right_turns, u_turns)