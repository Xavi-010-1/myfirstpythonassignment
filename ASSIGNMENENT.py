# 🎉 Welcome to the Fun Calculator! 🎉
# Let's do one operation at a time like a pro! 😎

# Step 1: Get the first number from the user
num1 = float(input("Enter the first number: "))

# Step 2: Get the second number from the user
num2 = float(input("Enter the second number: "))

# Step 3: Ask for the operation
print("Choose an operation: + for addition, - for subtraction, * for multiplication, / for division")
operation = input("Enter the operation: ")

# Step 4: Perform the chosen operation and show the result
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Oops! You can't divide by zero. 🤯")
else:
    print("Invalid operation. Please choose +, -, * or /. 🚫")

# 🎊 Done! You've just used your very own calculator! 💪🧮