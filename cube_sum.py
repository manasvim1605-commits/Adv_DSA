n=int(input("Enter the no.of natural numbers "))
sum=0
i=1
for i in range(n+1):
    sum=sum+(i*i*i)
print("Sum is ",sum)