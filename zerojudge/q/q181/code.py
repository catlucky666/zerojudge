a , b = map(int , input().split())
n = int(input())
t = (map(int , input().split()))
c = a + b
to = 0
for i in t:
    k = i % c
    if(k >= a):
        to += b - (k - a)
print(to)