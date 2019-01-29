snappers = [False for n in range(200)]

def toggle(i,n):
    if(snappers[i] == False):
        snappers[i] = True
        return
    else:
        snappers[i] = False
        toggle(i+1,n)

def main():
    for i in range(int(input())):
        if(i > 0):
            print("")
        n,k = list(map(int,input().split()))
        for j in range(k):
            toggle(0,n)
        result = "ON" if (False not in snappers[:n]) else "OFF"
        print("Case #%d: %s" %((i+1),result),end="")
        for ii in range(len(snappers)):
            snappers[ii] = False
        
main()
