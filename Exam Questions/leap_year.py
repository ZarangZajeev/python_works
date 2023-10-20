# for year in range(1800,2025):
#     if(year % 4==0 and year % 100 !=0) or (year % 400==0):
#         print(year)

# year=int(input("Enter a year: "))
# if( year % 4==0 and year % 100!=0) or (year % 400==0):
#     print(f"{year}  is leap year")
# else:
#     print(f"{year} is not leap year")

year=int(input("Enter a year: "))
if( year % 4==0 and year %100!=0) or (year % 400==0):
    print(f"This year is leap year")
else:
    print(f"this is not leap year")