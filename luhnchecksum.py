for i in range(int(input())):
    total = 0
    check = input()[::-1]
    total += int(check[0])
    for i in range(1,len(check)):
        if(i%2 == 0):
            total += int(check[i])
        else:
            digit = 2*int(check[i])
            if(digit > 9):
                digit -= 10
                digit += 1
            total += digit
    if((total%10) == 0):
        print("PASS")
    else:
        print("FAIL")
