#Write a function that returns the maximum of two numbers.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def max_num(x,y):
    result = print('Maximum num is :',max(x,y))
    return result
    
max_num(num1,num2)