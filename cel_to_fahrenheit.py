#Celsius to Fahrenheit
"""Formula:(0°C × 9/5) + 32 = 32°F"""

Cel = float(input("Enter temperature in Celsius : "))
degInFahrenheit = (Cel * 1.8) + 32

print(f"{Cel}°C is equal to {degInFahrenheit}°F")