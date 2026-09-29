n=int(input("Enter a number "))
temp=n
sum=0
while(temp!=0):
    temp=temp%10
    sum=sum+temp
    temp=temp//10
print("Sum is ",sum)