#Print all prime numbers in an interval.

lower_interval = int(input("Enter lower interval : "))
upper_interval = int(input("Enter upper interval : "))

print(f"\nPrime numbers from {lower_interval} to {upper_interval} are : ")
for num in range(lower_interval,upper_interval+1):     #make certain range for above given numbers.
    if num > 1:                                        #since prime number is greater than 1.
        for i in range(2,num):                         #condition for not a prime number.
            if num % i == 0:                           #   "       "   "  "   "     "  
                break
        else:                                          #condition for a prime number.
            print(num)