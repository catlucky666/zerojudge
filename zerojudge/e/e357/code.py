def F(x):
  if x == 1:
    return 1
  elif x % 2 == 0:
    return F(x // 2)
  else:
    return F(x - 1) + F(x + 1)
x = int(input())
result = F(x)
print(result)