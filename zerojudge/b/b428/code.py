while True:
    try:
        a = input()
        b = input()
        k = 0
        ascii_a = ord(a[0])
        ascii_b = ord(b[0])
        k = ascii_b - ascii_a
        if k < 0:
          k = k + 26
        print(k)
    except EOFError:
        break