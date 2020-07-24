#Armstrong Number
"""An Armstrong number is an n-digit base b number such that the sum of its (base b) digits raised to the power n is the number itself.
Eg: 407 is sum of cube of three num i.e.4,0,7 && 1634 is sum of ^4 of 4 num i.e.1,6,3,4"""

#import math
n = int(input("Enter number : "))
order = len(str(n))
#order = int(math.log10(n))+1  #adding 1 gives number of digits
sum = 0

temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** order
    temp //= 10

if sum == n:
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")
