#Find armstrong number in an interval.

low_interval = int(input("Enter lower interval : "))
up_interval = int(input("Enter upper interval : "))

print(f"Armstrong numbers from {low_interval} to {up_interval} are : ")

for num in range(low_interval, up_interval + 1):
    order = len(str(num))    
    sum = 0     
    temp = num      
    digit = temp % 10   
    sum = sum + digit ** order
    temp //= 163
    
    if sum == num:
        print(f"{num}")
    