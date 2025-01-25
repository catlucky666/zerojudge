s, t, n, m, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(s)]
B = [list(map(int, input().split())) for _ in range(n)]

符合條件的子矩陣數 = 0
最小差異 = float('inf')
A_sum = sum(sum(row) for row in A)  # 計算 A 的總和

for i in range(n - s + 1):
    for j in range(m - t + 1):
        dis = 0
        B_sum = 0
        for x in range(s):
            for y in range(t):
                if A[x][y] != B[i + x][j + y]:
                    dis += 1
                B_sum += B[i + x][j + y]
                # 若距離超過 r，提前跳出內層迴圈
                if dis > r:
                    break
            if dis > r:
                break
        if dis <= r:
            符合條件的子矩陣數 += 1
            差異 = abs(A_sum - B_sum)
            if 差異 < 最小差異:
                最小差異 = 差異

print(符合條件的子矩陣數)
print(最小差異 if 符合條件的子矩陣數 > 0 else -1)