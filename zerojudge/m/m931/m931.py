n = int(input())
A = []
for i in range(n):
    atk , def_ = map(int , input().split())
    b = atk ** 2 + def_ ** 2
    A.append((b , atk , def_))
A.sort(reverse = True)
sec = A[1]
print(sec[1] , sec[2])
