def find(N, M, A_t, B_t, D):
  for i in range(N):
    for j in range(M):
      a_s, a_e = A_t[i]
      b_s, b_e = B_t[j]
      common_start = max(a_s, b_s)
      common_end = min(a_e, b_e)
      if common_end - common_start >= D:
        return common_start, common_start + D
  return -1, -1
N, M = map(int, input().split())
A_t = []
for k in range(N):
  start, end = map(int, input().split())
  A_t.append((start, end))
B_t = []
for l in range(M):
  start, end = map(int, input().split())
  B_t.append((start, end))
D = int(input())
start, end = find(N, M, A_t, B_t, D)
if start == -1:
  print(start)
else:
  print(start, end)