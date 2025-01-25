n = int(input())
m3_0 = 0
m3_1 = 0
m3_2 = 0
for i in range(n):
    a = int(input())
    if(a % 3 == 0):
        m3_0 += 1
    elif(a % 3 == 1):
        m3_1 += 1
    elif(a % 3 == 2):
        m3_2 += 1
print(m3_0 , m3_1 , m3_2)