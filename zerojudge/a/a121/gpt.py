from math import sqrt, ceil

def simple_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 和 1 不是質數
    for i in range(2, int(sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

def segmented_sieve(a, b):
    limit = int(sqrt(b)) + 1
    primes = simple_sieve(limit)
    
    is_prime = [True] * (b - a + 1)
    
    for p in primes:
        start = max(p * p, ceil(a / p) * p)
        for j in range(start, b + 1, p):
            is_prime[j - a] = False
    
    if a == 1:
        is_prime[0] = False  # 1 不是質數
    
    return sum(is_prime)

while True:
    try:
        a, b = map(int, input().split())
        print(segmented_sieve(a, b))
    except EOFError:
        break