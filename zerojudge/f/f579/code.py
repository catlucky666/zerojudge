a , b = map(int , input().split())
n = int(input())
A = []
c = 0
for i in range(n):
    l = list(map(int , input().split()))
    A.append(l[:-1])
for i in A:
    c_a = 0
    c_b = 0
    for j in i:
        if(j == a):
            c_a += 1
        elif(j == -a):
            c_a -= 1
        elif(j == b):
            c_b += 1
        elif(j == -b):
            c_b -= 1
    if(c_a > 0 and c_b > 0):
        c += 1
print(c)