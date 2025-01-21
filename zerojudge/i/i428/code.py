n = int(input())
stations = []
M = 0
m = float('inf')
for i in range(n):
    x, y = map(int , input().split())
    stations.append((x, y))
for i in range(n - 1):
    x1, y1 = stations[i]
    x2, y2 = stations[i + 1]
    dis = abs(x2 - x1) + abs(y2 - y1)
    if dis > M:
        M = dis
    if dis < m:
        m = dis
print(M , m)