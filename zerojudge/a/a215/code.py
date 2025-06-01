while True:
    try:
        n , m = map(int , input().split())
        i = n
        s = 0
        while True:
            s += n
            n += 1
            if(s > m):
                break
        print(n - i)
    except EOFError:
        break