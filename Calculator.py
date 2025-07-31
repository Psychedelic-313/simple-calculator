num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

#Perform the operation and display the result
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
      print("Error: Can't Divide by zero.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
      