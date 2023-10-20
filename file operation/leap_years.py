years=open("D:\\MY PC\\july_python_works\\file operation\\years.txt","w")
for y in range(1800,2025):
    years.write(str(y)+"\n")
years.close()

years=open("D:\\MY PC\\july_python_works\\file operation\\years.txt","r")
leap_year_print=open("D:\\MY PC\july_python_works\\file operation\\leap_year_print.txt","w")
for y in years:
    if (int(y) % 4==0 and int(y) % 100!=0) or (int(y) % 400==0):
        leap_year_print.write(str(y))
years.close()
leap_year_print.close()