# Factorial program

number = int(input("Enter a number: "))

factor = 1

for i in range(1, number + 1):
    factor = factor * i

print("Factorial of a given number :", factor)