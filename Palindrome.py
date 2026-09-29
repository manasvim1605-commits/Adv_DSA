num=int(input("Enter a number "))
sum=0
n=num
while(num>0):
    sum=sum*10+(num%10)
    num//=10
if(n==sum):
    print("Palindrome number")
else:
    print("not a Palindrome number")