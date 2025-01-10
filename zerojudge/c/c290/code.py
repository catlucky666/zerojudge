x = int(input())
odd = 0
even = 0

a = str(x)
b = len(a)
for i in range(b):
    c = a[i]
    d = int(c)
    if i % 2 == 0:
        odd += d
    else:
        even += d
      
sum = abs(odd - even)
print(sum)