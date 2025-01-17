h1, m1 = map(int , input().split())
h2, m2 = map(int , input().split())
H = h2 - h1
M = m2 - m1
if(M < 0):
    M = M + 60
    H = H - 1
if(H < 0):
    H = H + 24
print(H , M)