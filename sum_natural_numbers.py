#Sum of natural numbers

num_terms = int(input("Enter number of terms : "))
for num in range(1,num_terms+1):
    result = int(num*(num+1) / 2)
print(f"Sum of {num_terms} natural number is : {result}")