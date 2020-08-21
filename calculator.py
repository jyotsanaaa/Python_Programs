#calculator
#number input
num1 = float(input('Enter the first number\t'))
num2 = float(input('Enter the second number\t'))
print("'Sum', 'Difference', 'Multiplication', 'Division'")
choice = input('Enter the calculation of your choice\t')
if (choice == 'Sum'):
    result = num1 + num2
elif (choice == 'Difference'):
    result = num1- num2
elif (choice == 'Multiplication'):
    result = num1 * num2
else:
    result = num1 / num2
#print result
if(result%2 == 0):
    print('The result is ',int(result))
else:
    print('The result is', result)