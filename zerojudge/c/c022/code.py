def odd_sum(a , b):
    tot = 0
    for num in range(a, b + 1):
        if num % 2 != 0:
            tot = tot + num
    return tot
T = int(input())
for case in range(1, T + 1):
    a = int(input())
    b = int(input())
    result = odd_sum(a, b)
    print(f"Case {case}: {result}")