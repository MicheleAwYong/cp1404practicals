"""
CP1404/CP5632 Practical - Suggested Solution
Make the appropriate choice of file-reading technique for each of these questions:
- read()
- readline()
- readlines()
- for line in file
"""

# 1. read()
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2. readline()
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3. readlines()
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. for line in file
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)