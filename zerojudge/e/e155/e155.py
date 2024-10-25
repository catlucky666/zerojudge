def game(n):
    c = list(range(1 , n + 1))
    dis = []
    while len(c) > 1:
        dis.append(c.pop(0))
        c.append(c.pop(0))
    re_c = c[0]
    dis_str = ", ".join(map(str , dis))
    print(f"Discarded cards: {dis_str}")
    print(f"Remaining card: {re_c}")
while True:
    n = int(input())
    if(n == 0):
        break
    game(n)