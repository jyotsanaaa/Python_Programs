#Find factorial of a number

num = int(input("Enter a number : "))
fact = 1
if num < 0:
    print("Please enter a positive number. Factorial doesn't exist for a negative number.")
elif num == 0:
    print("Factorial of {num} is : 1")
else:
    for i in range(1,num+1):
        fact = fact * i 
    print(f"Factorial of {num} is : {fact}." )

