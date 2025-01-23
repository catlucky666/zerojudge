a, b = map(int, input().split())  # 輸入範圍 a 和 b
results = []  # 用於存儲所有符合條件的阿姆斯壯數

for num in range(a, b):  # 遍歷範圍內的每個數字
    stra = str(num)  # 將數字轉為字串
    la = len(stra)  # 計算數字的位數
    t = 0
    for j in range(la):  # 遍歷數字的每一位
        t += int(stra[j]) ** la  # 累加每一位的次方
    if t == num:  # 如果累加結果等於該數字本身
        results.append(num)  # 將該數字加入結果列表

# 輸出結果
if results:  # 如果找到阿姆斯壯數
    print(" ".join(map(str, results)))  # 以空格分隔輸出
else:  # 如果範圍內沒有阿姆斯壯數
    print("none")