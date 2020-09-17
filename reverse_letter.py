#Reverse letter in a word

user_ip = str(input("Enter a word : "))

def func(x):
    res = ''.join(reversed(x))
    print(res)

func(user_ip)