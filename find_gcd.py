#Find HCF or GCD

print('---Using Euclidean Algorithm---')

num1 = int(input("Enter smallest number : "))
num2 = int(input("Enter highest number : "))

def function(n1,n2):
    while(n2):
        n1, n2 = n2,n1%n2
    return n1

gcd = function(num1,num2)
print(f'\nGCD of {num1} and {num2} is : {gcd}')