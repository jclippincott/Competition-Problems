for i in range(int(input())):
    line = list(map(int,input().split()))
    for i in range(1,len(line)-1):
        if(line[i]+1 != line[i+1]):
            print(i+1)
            break
