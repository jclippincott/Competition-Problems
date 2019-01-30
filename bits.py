for i in range(int(input())):
    currstring = ""
    max1s = 0
    for char in input():
        currstring += char
        count1s = str(bin(int(currstring))).count("1")
        if(count1s > max1s):
            max1s = count1s
    print(max1s)
