n = (input())
a_n = [ord(char) for char in n]
b = []
for i in range(6):
    d = abs(a_n[i + 1] - a_n[i])
    b.append(d)
print("".join(map(str , b)))   #