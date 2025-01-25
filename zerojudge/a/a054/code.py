dic = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34,
    'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25,
    'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33
}
w = [8 , 7 , 6 , 5 , 4 , 3 , 2 , 1]
ID = input()
c_l = []
for l in dic:
    n = dic[l]
    f = n // 10
    s = n % 10
    w_s = 0
    w_s = f * 1 + s * 9
    for i in range(8):
        w_s += int(ID[i]) * w[i]
    if((10 - (w_s % 10)) % 10 == int(ID[8])):  #
        c_l.append(l)
print("".join(c_l))                            #