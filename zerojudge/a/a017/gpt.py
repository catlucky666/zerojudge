import sys
import re

def co(a, b, op):  # 基本運算函式
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b  # 整數除法，避免浮點數
    if op == '%':
        return a % b
    return 0

def tokenize(expression):  # 分割運算式
    return re.findall(r'\d+|[+*/%()-]', expression)

def pri(op):  # 定義運算符優先級
    if op in ('+', '-'):
        return 1
    if op in ('*', '/', '%'):
        return 2
    return 0

def infix_to_postfix(tokens):  # 中序轉後序
    output = []
    operators = []
    for token in tokens:
        if token.isdigit():  # 如果是數字，直接加入輸出
            output.append(int(token))
        elif token == '(':
            operators.append(token)  # 左括號壓入堆疊
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())  # 彈出運算符
            operators.pop()  # 移除左括號
        else:  # 處理運算符
            while (operators and operators[-1] != '(' and pri(operators[-1]) >= pri(token)):
                output.append(operators.pop())
            operators.append(token)
    while operators:  # 處理堆疊剩餘的運算符
        output.append(operators.pop())
    return output

def main():
    for l in sys.stdin:  # 持續讀取直到 EOF
        l = l.strip()
        if not l:  # 跳過空行
            continue

        # 分割運算式並轉換為後序
        tokens = tokenize(l)
        postfix = infix_to_postfix(tokens)

        # 直接在此處計算後序結果
        stack = []
        for token in postfix:
            if isinstance(token, int):  # 數字壓入堆疊
                stack.append(token)
            else:  # 運算符，取出兩個操作數
                b = stack.pop()
                a = stack.pop()
                stack.append(co(a, b, token))

        # 堆疊中最後一個值即為結果
        print(stack[0])

if __name__ == "__main__":
    main()