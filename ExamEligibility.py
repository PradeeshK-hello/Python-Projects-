working_days = int(input("Enter the number of working days:"))
absent_days = int(input("Enter the number of days absent:"))

days_present = working_days - absent_days
percentage = (days_present / working_days) * 100

if percentage < 75:
    print("Unfortunately, you are not eligible for the exam. Please contact admin for more info.")
else:
    print("Congratulations! You are eligible for the exam. Good Luck!")