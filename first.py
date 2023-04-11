#math functions

def addiction(first, second):
    return int(first) + int(second)

def substraction(first, second):
    return int(first) - int(second)

def multiplication(first, second):
    return int(first) * int(second)

def power(first, second):
    return int(first) ** int(second)
def divide(first, second):
    return int(first) / int(second)

#input statement

firstNumber = input("Write first number: ")
operation = input("Write operation you want to do (+, -, *, ^, /): ")
secondNumber = input("Write second number: ")


#functions calls with "match"
match operation:
    case "+":
        result = addiction(firstNumber, secondNumber)
    case "-":
        result = substraction(firstNumber, secondNumber)
    case "*":
        result = multiplication(firstNumber, secondNumber)
    case "^":
        result = power(firstNumber, secondNumber)
    case "/":
        if secondNumber != 0:
            result = divide(firstNumber, secondNumber)
        else:
            result = "fail"
    case _:
        result = "fail"

#printing result if its good
if result == "fail":
    print("You writed wrong operation")
else:
    print("Result of",firstNumber,operation,secondNumber,"is", result)

