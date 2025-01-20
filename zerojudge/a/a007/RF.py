from sympy import isprime
while True:
    try:
        n = int(input())
        if(isprime(n)):
            print("質數")
        else:
            print("非質數")
    except EOFError:
        break