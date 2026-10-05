num=0
n= int(input("Enter no. of rows: "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+num), end=" ")
        num+=1
    print()