#Fibonacci Series
numT = int(input("Enter number of terms: "))
num1 = 0
num2 = 1
n = 0

if numT < 0:
    print("Please enter a positive number.")
elif numT == 1:
    print(num2)
else:
    while n < numT:
        print(num2)
        sum = num1 + num2
        num1 = num2
        num2 = sum
        n += 1
