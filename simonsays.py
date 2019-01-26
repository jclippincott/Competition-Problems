for i in range(int(input())):
    line = input()
    if((len(line) > 10) and (line[:10] == "Simon says")):
        print(line[10:])
    
