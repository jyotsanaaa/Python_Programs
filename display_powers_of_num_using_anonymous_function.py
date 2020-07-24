#Display Powers of 2 Using Anonymous Function

num = 2
num_terms = int(input("Enter number of terms : "))

#anonymous function
result = list(map(lambda x : 2 **x,range(num_terms+1)))

for i in range(1,num_terms + 1):
    print(f"2 ^ {i} : ", result[i])
    