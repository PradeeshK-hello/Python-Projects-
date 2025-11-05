number= int(input("Enter a number:"))

if number>50:
    print("The number is greater than 50.")
    if number%2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("The numbe is less than or equal to 50.")