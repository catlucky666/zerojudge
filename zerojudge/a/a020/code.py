id = input()
dict = {"A": 10, "J": 18, "S": 26, "B": 11, "K": 19, "T": 27, "C": 12, "L": 20, "U": 28, "D": 13, "M": 21, "V": 29, "E": 14,"N": 22, "W": 32, "F": 15, "O": 35, "X": 30, "G": 16, "P": 23, "Y": 31, "H": 17, "Q": 24, "Z": 33, "I": 34, "R": 25}
num = dict[id[0]]
num1 = num // 10 
num2 = num % 10 
total = num1 + num2 * 9 + int(id[9])
for i in range(1, 9):
    total = total + int(id[i]) * (9 - i)
if(total % 10 == 0):
    print("real")
else:
    print("fake")