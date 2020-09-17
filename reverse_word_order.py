#Reverse word in order from a sentence

user = str(input("Enter any sentence : "))

def reverse_word(x):
    y = x.split()
    result = "".join(reversed(y))
    print("Reversed order of the given sentence is :",result)
    
reverse_word(user)