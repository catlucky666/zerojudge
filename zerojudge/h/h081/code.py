n, D = map(int, input().split())
a = list(map(int, input().split()))
c = 1
p = 0
l = a[0]
for i in range(1, n):
    if(c == 1 and a[i] >= l + D):
        c = 0
        p += a[i] - l
        l = a[i]
    elif(c == 0 and a[i] <= l - D):
        c = 1
        l = a[i]
print(p)