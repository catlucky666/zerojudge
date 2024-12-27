m , d = map(int , input().split())
s = (m * 2 + d) % 3
if (s == 0):
  f = "普通";
elif (s == 1):
  f = "吉"
else:
  f = "大吉"
print(f)