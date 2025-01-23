while True:
    try:
        n = int(input())
        r = n ** 2 - n + 2
        print(r)
    except EOFError:
        break