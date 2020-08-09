#Sum of natural numbers using recursion

def sum_recurs(n):
    if n <= 1:
        return n
    else:
        return n + sum_recurs(n - 1)

num = int(input("Enter a positive number : "))

if num < 0:
    print("Please enter a positive number!!")
else :
    print(f"Sum of {num} natural number is :",sum_recurs(num)) 