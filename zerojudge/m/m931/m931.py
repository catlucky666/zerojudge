n = int(input())
A = []
for i in range(n):
    atk , Def = map(int , input().split())
    b = atk ** 2 + Def ** 2
    A.append((b , atk , Def))
A.sort(reverse = True)
sec = A[1]
print(sec[1] , sec[2])
