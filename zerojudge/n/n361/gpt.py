import math
n = int(input())
a = list(map(int, input().split()))
def num(a):
  def squ(x):
    s = int(math.sqrt(x))
    return s * s == x
  if a % 3 == 0 and a % 2 == 0:
    return 1
  elif a % 2 == 1 and a % 3 != 0:
    return 2
  elif squ(a) or (a % 2 == 0 and a % 7 != 0):
    return 3
  else:
    return 0
nums = [num(room) for room in a]
print(" ".join(map(str, nums)))