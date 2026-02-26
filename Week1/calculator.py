# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Division by zero is not ok"
    return a / b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Plz afno operation choose garnus:")
print("1. Add garne ? 1 press")
print("2. Subtract garne? 2 press")
print("3. Multiply garne? 3 press")
print("4. Divide garne ? 4 press")

choice = input("Enter your choice 1 kita 2 kita 3 kita 4: ")

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("1-4 matra allowed xha dhanyabad")