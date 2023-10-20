weight=input("Enter weight in Kg: ");
height=input("Enter height in CM: ");
height_m=int(height)/100;
bmi=int(weight)/(height_m**2);
print(f"BMI= {bmi}");
if (bmi<18.5):
    print("Under weight");
elif(18.5<= bmi <=24.9):
    print("Normal weight");
elif(25.0<= bmi <=29.9):
    print("Overweight");
elif(30.0<=bmi<=34.9):
    print("Obesity (Class I)");
elif(35.0<=bmi<=39.9):
    print("Obesity (Class II)");
elif bmi>40.0:
    print("Obesity (Class III)");