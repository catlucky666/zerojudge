n = int(input())
for i in range(n):
    a , b , c = map(int , input().split())
    if(a == 1):
        d = b + c
    elif(a == 2):
        d = b - c
    elif(a == 3):
        d = b * c
    elif(a == 4):
        d = b / c
    print(int(d))