s , t , n , m , r = map(int , input().split())
A = []
B = []
for _ in range(s):
    row = list(map(int , input().split()))     #
    A.append(row)
for _ in range(n):
    row = list(map(int , input().split()))     #
    B.append(row)                              
c = 0                                          
min_dif = float('inf')                         #
A_sum = sum(sum(row) for row in A)             #
for i in range(n - s + 1):                     
    for j in range(m - t + 1):                 
        dis = 0
        B_sum = 0
        for x in range(s):
            for y in range(t):
                if A[x][y] != B[i + x][j + y]: 
                    dis += 1
                B_sum += B[i + x][j + y]       
        if dis <= r:
            c += 1
            dif = abs(A_sum - B_sum)           
            if dif < min_dif:
                min_dif = dif
print(c)
print(min_dif if c > 0 else -1)                #