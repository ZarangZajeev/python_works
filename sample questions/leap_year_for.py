for year in range(1800,2025):
    if (year % 4 ==0 and year % 100 !=0) or ( year % 400==0):
        print(year);