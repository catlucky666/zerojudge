l, q, r = map(int, input().split())
st = input()
s = []
for _ in range(q):
    n_s = [''] * l
    a = list(map(int, input().split()))
    for j in range(l):
        n_s[a[j] - 1] = st[j]
    st = ''.join(n_s)
    s.append(st)
for i in range(r):
    for j in range(q):
        print(s[j][i], end='')
    print()