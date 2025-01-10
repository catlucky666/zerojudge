A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
n = int(input())
max_sum = float('-inf')
for X1 in range(n + 1):
    X2 = n - X1
    Y1 = A1 * X1 ** 2 + B1 * X1 + C1
    Y2 = A2 * X2 ** 2 + B2 * X2 + C2
    max_sum = max(max_sum, Y1 + Y2)
print(max_sum)