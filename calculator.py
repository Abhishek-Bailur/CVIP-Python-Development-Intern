def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def main(): 
    number_1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, or /): ")
    number_2 = float(input("Enter the second number: "))
    result = None
  
    if operator == "+":
        result = add(number_1, number_2)
    elif operator == "-":
        result = subtract(number_1, number_2)
    elif operator == "*":
        result = multiply(number_1, number_2)
    elif operator == "/":
        result = divide(number_1, number_2)
    if result is not None:
        print("The result is:", result)
    else:
        print("Invalid operator")

if __name__ == "__main__":
    main()

