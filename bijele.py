cset = [1,1,2,2,2,8]
pieces = [int(x) for x in input().split()]

for i in range(6):
    if(i > 0):
        print(" ",end="")
    print("%d" %(cset[i]-pieces[i]), end="")
