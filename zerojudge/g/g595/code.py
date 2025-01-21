n = int(input())
h = 0
a = list(map(int, input().split()))
if a[0] == 0:
  a[0] = a[1]
  h += a[0]
if a[n - 1] == 0:
  a[n - 1] = a[n - 2]
  h += a[n - 1]
for i in range(1, n - 1):
  if a[i] == 0:
    a[i] = min(a[i - 1], a[i + 1])
    h += a[i]
print(h)