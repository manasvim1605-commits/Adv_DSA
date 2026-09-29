n=int(input("Enter a number "))
temp=n
sum=0
while(temp!=0):
    ld=temp%10
    sum=sum+ld
    temp=temp//10
print("Sum is ",sum)