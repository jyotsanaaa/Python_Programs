#Make A Simple Calculator

print("---Simple Calculator---\n")
n1 = int(input("Enter first number : "))
operator = input("Enter operator(eg:+,-,*,/) : ")
if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "%":
    print("Please enter a valid operator.")

n2 = int(input("Enter second number : "))
if operator == '+':
    print(f"\nSum of {n1} and {n2} is :",n1+n2)
elif operator == '-':
    print(f"\nDifference of {n1} and {n2} is :",n1-n2)
elif operator == '*':
    print(f"\nProduct of {n1} and {n2} is :",n1*n2)
else:
    print(f"\nDivision of {n1} and {n2} is :",n1/n2)

        
