#Factors of a number

num = int(input("Enter any number : "))

print(f"Factorial of {num} are : ")
for i in range(1,num+1):
    if num % i == 0:
        print(i)
    