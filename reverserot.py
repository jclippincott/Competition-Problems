line = input().split()
vals = {}
chars = {}
for i in range(26):
    vals[chr(i+65)]=i
    chars[i] = chr(i+65)
vals['_'] = 26
chars[26] = '_'
vals['.'] = 27
chars[27] = '.'

while (line[0] != "0"):
    shift = int(line[0])
    copy = ""
    for char in line[1][::-1]:
        copy += chars.get((vals.get(char)+shift)%28)
    print(copy)
    line = input().split()
