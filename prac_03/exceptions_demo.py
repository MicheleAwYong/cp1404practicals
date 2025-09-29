"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It happens if there is no whole number inputted, such as a number with a decimal, word or letter.
2. When will a ZeroDivisionError occur?
It happens when I inputted a 0 into the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


"The modified code"
try:
    numerator = int(input("Enter the numerator: "))
    while True:
        denominator = int(input("Enter the denominator: "))
        if denominator != 0:
            break
        else:
            print("Cannot divide by zero! Please enter a non-zero denominator.")
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")