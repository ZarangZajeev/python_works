def factorial(num):
    fact=1
    i=1
    while(i<=num):
        fact=fact*i
        i+=1
    return fact

print(factorial(6))