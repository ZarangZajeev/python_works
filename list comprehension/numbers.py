lst=[i for i in range(1,8)]
print(lst)
day=[f"{i} is Holiyday" if i in (1,7) else f"{i} is Weekday" for i in range(1,8)]
print(day)