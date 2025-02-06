s = input()
ls = len(s)
for i in range(0 , ls):
    print(s[i:] + s[:i])     #