#R(n) = 1 +ขั(n , 1) +C(n , 2) + C(n , 3)
while True:
    try:
        n = int(input())
        r = (n ** 3 + 5 * n + 6) / 6
        print(int(r))
    except EOFError:
        break