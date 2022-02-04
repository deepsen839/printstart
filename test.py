def printStar():
    endline =0
    for i in range(10,0,-1):
        if i%2==0 and i!=0:
            endline = endline+2
            j =int(i/2-1)
        for k in range(0,j):
            print(" ",end="")
        print(endline*"*",end="")
        print(j*" ") 
        print("\n")
        
printStar()