n = int(input())
s = 0
if(n < 10):
    s = 6 * n
elif(n < 20):
    s = 6 * 10 + 2 * (n - 10) 
elif(n <= 40):
    s = 6 * 10 + 2 * 10 + 1 * (n - 20)
else:
    s = 100
print(s)