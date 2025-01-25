import math
x_man, y_man = map(int, input().split())
n = int(input())

min_distance = float('inf')
nearest_fish = (0, 0)
for i in range(n):
    x_fish, y_fish = map(int, input().split())
    distance = math.sqrt((x_fish - x_man) ** 2 + (y_fish - y_man) ** 2)
    if distance < min_distance:
        min_distance = distance
        nearest_fish = (x_fish, y_fish)

print(nearest_fish[0], nearest_fish[1])