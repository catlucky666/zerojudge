while True:
    try:
        n = int(input())
        i = 2
        k = []
        while(i * i <= n):
            while(n % i == 0):
                k.append(i)
                n = n // i
            i += 1
        if(n > 1):
            k.append(n)
        s = sum(k)
        print(s)
    except:
        break