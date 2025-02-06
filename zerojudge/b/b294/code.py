n = int(input())
k = list(map(int , input().split()))
p = []
p = list(range(1, n + 1))                 #
t = 0
for i in range(n):
    t += k[i] * p[i]
print(t)