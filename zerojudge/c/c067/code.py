c = 1
while True:
    n = int(input())
    if n == 0:
        break
    str = input().strip().split()
    a = [int(num) for num in str]
    tot = sum(a)
    ave = tot / n
    min_move = sum(abs(ele - ave) for ele in a)
    min_move = min_move / 2
    print(f"Set #{c}")
    print(f"The minimum number of moves is {int(min_move)}.")
    count += 1