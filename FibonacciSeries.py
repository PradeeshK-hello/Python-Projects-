num_of_times = int(input("Enter the number of times: "))

num1 = 0
num2 = 1

print(num1)
print(num2)

for i in range(num_of_times):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)