n=int(input("Enter a number "))
temp=n
sum=0
while(temp!=0):
    ld=temp%10
    cube=ld*ld*ld
    sum=sum+cube
    temp=temp//10
if(n==sum):
    print("Armstrong number")
else:
    print("not an Armstrong number")