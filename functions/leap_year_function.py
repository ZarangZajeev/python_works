def leap_year(year):
    if(year%4==0 and year%100 !=0) or (year==400):
        return(f"{year} is leap year")
    else:
        return(f"{year} is not leap year")
    
print(leap_year(2023))