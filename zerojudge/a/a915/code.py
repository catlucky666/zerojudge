n = int(input())
p = []
for i in range(n):
    a , b = map(int , input().split())
    p.append((a , b))
s = sorted(p)
for i , j in s:
    print(i , j)