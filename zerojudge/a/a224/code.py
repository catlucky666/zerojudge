import sys                      #
def can_form_palindrome(s):
    char = set()
    for c in s:
        if c.isalpha():
            c = c.lower()
            if c in char:
                char.remove(c)
            else:
                char.add(c)
    return len(char) <= 1
for line in sys.stdin:          #
    line = line.strip()
    if can_form_palindrome(line):
        print("yes !")
    else:
        print("no...")