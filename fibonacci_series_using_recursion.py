#Display Fibonacci Sequence Using Recursion

def fib_reoccurs(n):
    if n <= 1:
        return n
    else:
        return (fib_reoccurs(n - 1) + fib_reoccurs(n - 2))


num_terms = int(input("Enter a positive number : "))

if num_terms <= 0:
    print("Please enter a positive number!!")
else:
    print("Fibonacci series : ")
    for i in range(num_terms):
        print(fib_reoccurs(i))