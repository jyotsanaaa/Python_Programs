print("Check if a number is prime")
#taking input from user
number = int(input('Enter the number\t'))

if number>1:

    for i in range(2,number):
        if(number%i) == 0:
            print(number, "is composite")
            print(i, "times",number//i,"is",number)
            break
    else:
        print(number, 'is a prime number')

else:
    print(number,'Number is not a prime number')