# movies=["Vigathakumaran","Marthanda","Balan", "Nirmala"]
# print(movies[0])
# print(movies[2])

# movies[1]="MArthanda Varma"
# print(movies)


expenses=[12000,11000,2400,2500,45000,36000,78000]
count=len(expenses)
print(expenses)
expenses[1]=15000
for i in range(0,count):
    print(expenses[i])

print()

total=sum(expenses)
print(f"Total expenses= {total}")

print()

total=0
for i in range(0,count):
    total=total+expenses[i]
print(f"Total = {total}")

print(sorted(expenses,reverse=True))
