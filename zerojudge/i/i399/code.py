from collections import Counter
A=[int(x) for x in input().split()]
m = Counter(A).most_common(1)[0][1]
print(m , end = ' ')
a = sorted(set(A) , reverse = True)
for i in a:
    print(i , end = ' ')