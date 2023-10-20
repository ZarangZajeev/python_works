year=int(input("Enter a year: "));
if (year % 4 ==0 and year % 100 !=0) or ( year % 400==0):
    print(f"{year} is leap year");
else:
    print(f"{year} is not leap year");


# if year%100==0 and year%400==0:
#     print(year)
# else year%100!=0 and year%4==0:
#     print(year)
