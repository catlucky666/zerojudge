n , d = map(int , input().split())
c = 0
t = 0
for i in range(n):
    p = list(map(int , input().split()))
    max_p = max(p)
    min_p = min(p)
    if max_p - min_p >= d:
        a = sum(p) // 3
        c += 1
        t += a
print(c , t)