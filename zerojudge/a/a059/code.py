T = int(input())
for i in range(T):
  a = int(input())
  b = int(input())
  num = 0
  for j in range(32):
    if(j ** 2) < a:
      continue;
    if(j ** 2) > b:
      break;
    num = num + j ** 2;
  print(f"Case {i + 1}: {num}")