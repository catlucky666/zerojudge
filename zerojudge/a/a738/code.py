while True:
    try:
        n , m = map(int , input().split())
        if(m > n):
            m , n = n , m
        while(n != 0):
            m , n = n , m % n
        print(m)
    except:
        break