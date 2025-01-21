from collections import Counter

# 讀取輸入並轉換為整數列表
A = [int(x) for x in input().split()]

# 計算眾數數量（出現最多次的數字的次數）
m = Counter(A).most_common(1)[0][1]
print(m, end=' ')

# 去除重複並由大到小排序
a = sorted(set(A), reverse=True)
print(" ".join(map(str, a)))