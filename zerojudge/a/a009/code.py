s = input()
decrypt = ""
for char in s:
    trans = chr( ord(char)-7 )
    decrypt = decrypt + trans
print(decrypt)