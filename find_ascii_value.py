#Find ASCII value of a character

print("To find ASCII value of a character")
string = str(input("Enter any character : "))
convert = ord(string)   #The ord() function returns an integer representing the Unicode character.
print(f"ASCII value of '{string}' is : {convert}")

print("\nTo find str from int value.")
num = int(input("Enter any number : "))
conv = chr(num)  #The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
print(f"String value of {num} is : '{conv}'")