print('Binary to Decimal Conversion')
print('Choose 1 for first method and 2 for second method')
choice = int(input('Enter the method\t'))
if (choice == 1):

# Method 1

    binaryinput = (input('Enter a binary number\t'))
    n = len(binaryinput)
    decimal = 0
    for x in binaryinput:
        decimal = decimal + int(int(x)*(2**(n-1)))
        n = n-1 
    print('The decimal value is',decimal)

else:

# Method 2

    binaryinput1 = int(input('Enter a binary number\t'))
    decimal1, i = 0, 0
    while (binaryinput1!=0):
        n = binaryinput1 % 10
        decimal1 = decimal1 + n * (2**i)
        binaryinput1 = binaryinput1//10
        i+=1
    print('The decimal value is',decimal1)   
