while True:
    try:
        n = list(map(int , input().split()))
        ln = len(n)
        s = sum(n[1:])     #
        a = s / (ln - 1)
        if(a > 59):
            print("no")
        else:
            print("yes")
    except EOFError:
        break