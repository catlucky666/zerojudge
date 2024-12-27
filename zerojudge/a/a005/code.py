n = int(input())
for _ in range(n):
    p = list(map(int, input().split()))
    if (p[1]-p[0] == p[2]-p[1]):
        ans = p[3] + (p[3]-p[2]) #p[4] = p[3]+d   
    else:
        ans = p[3] * (p[3]//p[2]) #p[4] = p[3]*r
    print(p[0], p[1], p[2], p[3], ans)