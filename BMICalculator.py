mass = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in cm:"))

BMI = mass / (height/100)**2

if BMI <= 18.4:
    print("UNDERWEIGHT")
elif BMI <= 24.9:
    print("HEALTHY")
elif BMI <= 29.9:
    print("OVERWEIGHT")
elif BMI <= 34.9:
    print("OBESE CLASS 1")
elif BMI <= 39.9:
    print("OBESE CLASS 2")
else:
    print("OBESE CLASS 3+")