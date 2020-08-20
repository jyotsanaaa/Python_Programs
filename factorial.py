print("Program to calculate Factorial of a number")

number = int(input('Enter the number\t'))

def factorial(number):

    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return (factorial(number - 1)) * number

print('The factorial is',factorial(number))

