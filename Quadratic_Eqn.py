#Solve quadratic equation
"""Quadratic equation is : a*x^2+b*x+c. Where a != 0(if a ==0, it is a linear equation)
It can be solved by : x = [-b (+-) sqrt(r)]/2a    (here r == b**2 - 4ac)
Condition for roots is :- 
if r > 0: there are two roots.
elif r == 0 : there is one root.
else there is no root i.e. discriminant < 0 """

import math
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
r = b**2 - 4*a*c    #This is discriminant.
if r > 0:
    x1 = (((-b) + math.sqrt(r)) / (2*a))
    x2 = (((-b) - math.sqrt(r)) / (2*a))
    print(f"There are two roots. They are : {x1} and {x2}")
elif r == 0 :
    x = ((-b)/(2*a))
    print(f"There is one root.That is : {x}")
else:
    print("There is no root.Dicriminant < 0")
