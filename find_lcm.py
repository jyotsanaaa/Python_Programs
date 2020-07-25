#Find LCM
#LCM Formula = (x*y)//gcd(x,y)

num1 = int(input("Enter lower num : "))
num2 = int(input("Enter greater num : "))

#To find GCD
def gcd(x,y):
    while(y):
        x,y = y, x%y
    return x

#To find LCM
def lcm(a,b):
    lcm = (a*b)//gcd(a,b)
    return lcm

print(f"LCM of {num1} and {num2} is :",lcm(num1,num2))