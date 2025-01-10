n = int(input())
w1, w2, h1, h2 = map(int, input().split())
v = list(map(int, input().split()))

# 計算每層的底面積
A1 = w1 * w1
A2 = w2 * w2

# 計算每層的最大容積
V1 = A1 * h1
V2 = A2 * h2

# 總水量
total_water = 0
max_height_change = 0
previous_height = 0

for water_volume in v:
    total_water += water_volume
    
    if total_water <= V1:  # 在第一層內
        current_height = total_water // A1
    elif total_water <= V1 + V2:  # 進入第二層
        current_height = h1 + (total_water - V1) // A2
    else:  # 水滿
        current_height = h1 + h2

    # 計算水位上升的變化量
    height_change = current_height - previous_height
    max_height_change = max(max_height_change, height_change)
    
    # 更新之前的高度
    previous_height = current_height

print(max_height_change)