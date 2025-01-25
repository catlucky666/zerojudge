n = int(input())
for i in range(n):
    k = input()
    r = 1
    for j in k:
        r *= int(j)
    print(r)