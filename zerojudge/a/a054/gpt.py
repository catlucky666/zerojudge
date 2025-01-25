# 字母對應表
letter_to_number = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34,
    'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25,
    'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33
}

# 輸入後9碼
ID = input()

# 確保輸入長度為9且為數字
if len(ID) == 9 and ID.isdigit():
    possible_letters = []  # 儲存符合條件的字母

    for letter, number in letter_to_number.items():
        # 拆分字母對應的數值
        first_digit = number // 10  # 十位數
        second_digit = number % 10  # 個位數

        # 加權計算
        weighted_sum = first_digit * 1 + second_digit * 9  # 字母部分
        weights = [8, 7, 6, 5, 4, 3, 2, 1]
        for i in range(8):  # 計算後8碼的加權總和
            weighted_sum += int(ID[i]) * weights[i]

        # 檢查是否符合條件
        if (10 - (weighted_sum % 10)) % 10 == int(ID[8]):
            possible_letters.append(letter)

    # 輸出符合條件的字母
    print("".join(possible_letters))