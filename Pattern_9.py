n= int(input("Enter no. of rows: "))
for i in range(n):
    print(" "*(n-i+1),end=" ")
    for j in range(2*i):
        if(j==0 or j==2*i):
            if(i==0 or i==n-1):
                print(chr(65+j), end=" ")
            else :
                print(" ")
    print()
    #       A
    #    A      C
    #  A           E
    #A  B  C  D  E  F  G