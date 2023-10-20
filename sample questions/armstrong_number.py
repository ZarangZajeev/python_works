num=input("Enter a number: ")
digit_len=len(num)
num=int(num)
num1=num
sum=0
while( num!=0):
    last_digit=num%10
    cube=last_digit**digit_len
    sum=sum+cube
    num=num//10
print(f"Sum of digit's power is {sum}")
if(num1==sum):
    print(f"The given number is Armstrong")
else:
    print(f"Given number is not Armstrong number")