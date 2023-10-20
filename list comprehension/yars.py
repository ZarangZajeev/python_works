years=[y for y in range(1800,2025)]
century=[cy for cy in years if cy%100==0]
print(century)

leap_years=[y for y in years if (y%100!=0 and y%4==0) or y%400==0]
print(leap_years)