print('Swap numbers using only two variables')

a = 5
b = 7

#before swap
print('Before Swap')
print('a =',a)
print('b =',b)
#Now we have to swap the values as a = 7 and b = 5

a+=b
b = a - b
a-=b
#after swap
print('After Swap')
print('a =',a)
print('b =',b)