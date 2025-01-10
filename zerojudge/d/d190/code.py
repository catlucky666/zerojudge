while True:
  n = int(input())
  if n == 0:
    break
  ages = list(map(int, input().split()))
  ages.sort()
  print(*ages)