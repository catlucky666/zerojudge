import re                                   #
while True:
    try:
        s = input().strip()
        w = re.findall(r'[a-zA-Z]+', s)     #
        print(len(w))
    except EOFError:
        break