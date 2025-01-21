n = int(input())
e = list(map(int , input().split()))
sum = (e[0] - 1) * 3

for i in range(1 , n):
    if e[i] > e[i - 1]:
        sum += (e[i] - e[i - 1]) * 3
    else:
        sum += (e[i - 1] - e[i]) * 2
print(sum)