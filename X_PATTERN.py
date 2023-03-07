n=int(input("Enter The Number: "))
m=n-1
for i in range(n):
    for s in range(i):
        print(end=" ")
    print(i+1,end="")
    if(i+1!=n):
        for ms in range(2*m-1):
            print(end=" ")
        print(i+1)
        m-=1
    else:
        print("")
for i in range(n-1,0,-1):
    for s in range(0,i-1,1):
        print(end=" ")
    print(i,end="")
    for ms in range(2*m+1):
        print(end=" ")
    print(i)
    m+=1