t = int(input())
for i in range(t):
    d = []
    for j in range(10):
        w , s = input().split()
        s = int(s)
        d.append([w, s])
    s_l = []
    for j in d:
        s_l.append(j[1])
    m = max(s_l)

    print(f"Case #{i + 1}:")
    for k in d:
        if(k[1] == m):
            print(k[0])