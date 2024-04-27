list=["s","o","i"]
count=len(list)
print(f"Given list {list} is pallindrome" if list==list[::-1] else f"{list} is not pallindrome, resultant list is {list[::-1]}")
print(count)