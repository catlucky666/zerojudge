k = int(input())
hs = 0
er = 0
T = []
S = []
def sum(hs , k , er):
  if((hs - k - 2 * er) < 0):
    return 0
  else:
    return (hs - k - 2 * er)
for _ in range(k):
  t , s = map(int , input().split())
  if(s == -1):
    er += 1
  T.append(t)
  S.append(s)
hs = max(S)
f = T[S.index(hs)]
print(sum(hs , k , er) , f)