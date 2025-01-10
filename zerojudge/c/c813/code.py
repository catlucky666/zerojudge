def dig_sum(n):
    return sum(int(dig) for dig in str(n))
def g(n):
    while n >= 10:
        n = dig_sum(n)
    return n
while True:
    n = int(input())
    if n == 0:
        break
    result = g(n)
    print(result)