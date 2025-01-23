a , b = map(int , input().split())
r = []
stra = str(a)
lena = len(stra)
for i in range(a , b):
    stra = str(i) 
    t = 0
    for j in range(len(stra)):    #
        t += int(stra[j]) ** len(stra)
    if(t == i):
        r.append(i)
if r:
    print(" ".join(map(str, r)))  #
else:
    print("none")