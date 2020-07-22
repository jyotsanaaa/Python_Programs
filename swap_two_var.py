#Swap Two Variables
num1 = float(input("Enter fist value : "))
num2 = float(input("Enter second value : "))

print("\nBefore swapping")
print(f"num1 = {num1}")
print(f"num2 = {num2}")

#Swapping
temp = num1
num1 = num2
num2 = temp
         
print("\nAfter swapping")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
