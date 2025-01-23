while True:
    try:
        n = int(input())
        bi = []
        while n > 0:
            r = n % 2
            bi.append(r)
            n = n // 2
        bi.reverse()
        result = ''.join(map(str, bi))
        print(result)
    except EOFError:
        break