expenses=12000,13000,11000,23000,24000,4000,45000

total=sum(expenses)
print(f"Total expense= {total}")

smalest=min(expenses)
print(f"Smalest expense= {smalest}")

largest=max(expenses)
print(f"Largest expense is = {largest}")

sort=sorted(expenses, reverse=True)
print(f"Expenses in decenting order= {sort}")