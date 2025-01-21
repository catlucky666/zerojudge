n = int(input())
a = [list(map(int , input().split())) for _ in range(2 * n)]
for i in range(n):
    u = a[2 * i]
    d = a[2 * i + 1]
    r = ''  
    if u[1] == u[3] or u[1] != u[5] or d[1] == d[3] or d[1] != d[5]:
        r += "A"
    if u[6] != 1 or d[6] != 0:
        r += "B"
    if u[1] == d[1] or u[3] == d[3] or u[5] == d[5]:
        r += "C"
    if r == '':
        print("None")
    else:
        print(r)