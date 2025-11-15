dig1 = int(input("Enter the first digit of your number: "))
dig2 = int(input("Enter the second digit of your number: "))
dig3 = int(input("Enter the third digit of your number: "))

if (dig1**3) + (dig2**3) + (dig3**3) == (dig1*100)+(dig2*10)+(dig3*1):
    print("This is an armstrong number.")
else:
    print("This is NOT an armstrong number.")