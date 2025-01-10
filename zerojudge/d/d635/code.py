while True:
    num = int(input())
    if num < 0:
        print("-1")
        break
    else:
        print(format(num, 'o'))