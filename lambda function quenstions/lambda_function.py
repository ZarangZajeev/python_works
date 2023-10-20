odd_even=lambda n: "Even number" if n%2==0 else "Odd number"
min_two=lambda n1,n2: n1 if n1<n2 else n2
num_check=lambda n:"Positive" if n>0 else "Negative"

print(odd_even(5))
print(min_two(9,23))
print(num_check(-6))