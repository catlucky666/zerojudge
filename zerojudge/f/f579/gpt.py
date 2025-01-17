a, b = map(int, input().split())
c = int(input())
X = 0
for _ in range(c):
    z = list(map(int, input().split()))  
    def count_occurrences(item):
        return z.count(item) - z.count(-item)

    count_a = count_occurrences(a)
    count_b = count_occurrences(b)

    if(count_a >= 1 and count_b >= 1):
        X += 1
print(X)