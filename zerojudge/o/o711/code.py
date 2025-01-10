n = int(input())
w1 , w2 , h1 , h2 = map(int , input().split())
A1 , A2= w1 * w1 , w2 * w2
V1 , V2= A1 * h1 ,A2 * h2
h_p = 0
t = 0
max_h = 0
v_n = list(map(int , input().split()))
for v in v_n:
    t += v
    if t <= V1:
        h = t // A1
    elif t <= V1 + V2:
        h = (t - V1) // A2 + h1
    else:
        h = h1 + h2   
    h_d = h - h_p
    if h_d > max_h:
        max_h = h_d
    h_p = h
print(max_h)