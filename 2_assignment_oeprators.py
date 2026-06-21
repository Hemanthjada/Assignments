

print("1. Basic Arithmetic Operations")


def basic_arithmetic(a, b):
    print("Addition :", a + b)
    print("Subtraction :", a - b)
    print("Multiplication :", a * b)
    if b != 0 :
        print("Division :", a / b)


basic_arithmetic(10, 5)

print("\n" + "=" * 50 + "\n")




def increment_decrement(number):
    print("Original value      :", number)

    number += 1
    print("After increment (+=1):", number)

    number -= 1
    print("After decrement (-=1):", number)


increment_decrement(10)

print("\n" + "=" * 50 + "\n")

# Check if Two Numbers are Equal

print("3. Check if Two Numbers are Equal")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

print("\n" + "=" * 50 + "\n")

# Relational Operators Demonstration

print("4. Relational Operators Demonstration")

print("num1 <  num2 :", num1 < num2)
print("num1 <= num2 :", num1 <= num2)
print("num1 >  num2 :", num1 > num2)
print("num1 >= num2 :", num1 >= num2)

print("\n" + "=" * 50 + "\n")

#  Find Smaller and Larger Numbers

print("5. Find Smaller and Larger Numbers")

if num1 < num2:
    print("Smaller number:", num1)
    print("Larger number :", num2)
elif num2 < num1:
    print("Smaller number:", num2)
    print("Larger number :", num1)
else:
    print("Both numbers are equal:", num1)

print("\n" + "=" * 50 + "\n")

# Combine Conditions (Largest of Three)

print("6. Combine Conditions - Largest of Three Numbers")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

print("\n" + "=" * 50 + "\n")

#  Operator-Based Calculator

print(" Operator-Based Calculator")

x = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
y = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", x + y)
elif operator == "-":
    print("Result:", x - y)
elif operator == "*":
    print("Result:", x * y)
elif operator == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator entered.")
