num=int(input("Enter a number: "))
result=0
current_number=0
i=1
while(i<=num):
    current_number=int(current_number)  * 10 + num
    print(current_number)
    result += current_number
    i+=1
print(f"The result is: {result}")  