print("My Calculator\n")

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function finds the power of a number
def power(x, y):
    return x ** y

# This function finds the remainder
def rem(x, y):
    return x % y

# This function divides two numbers and finds its GIF
def GIF_of_quotient(x, y):
    return x // y


print("Select an Operator:\n")
print("1. Addition +\n")
print("2. Subtraction -\n")
print("3. Multiplication *\n")
print("4. Division /\n")
print("5. Power **\n")
print("6. Remainder %\n")

while True:
    # take input from the user
    choice = input("Enter choice of operator from 1 to 6: ")

    # check if choice is one of the four options 
    if choice in ('1', '2', '3', '4','5','6'):
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", subtract(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))

        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))

        elif choice == '5':
            print(a, "**", b, "=", power(a, b))   

        elif choice == '6':
            print(a, "%", b, "=", rem(a, b))     
        
        # check if user wants another calculation and break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation.lower() == "n" or "no":
          break
    
    else:
        print("Invalid input, please try again.")

