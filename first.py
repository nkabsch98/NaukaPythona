def addiction(first, second):
    return int(first) + int(second)

def substraction(first, second):
    return int(first) - int(second)

def multiplication(first, second):
    return int(first) * int(second)

def power(first, second):
    return int(first) ** int(second)



firstNumber = input("Write first number: ")
operation = input("Write operation you want to do (+, -, *, ^): ")
secondNumber = input("Write second number: ")



match operation:
    case "+":
        result = addiction(firstNumber, secondNumber)
    case "-":
        result = substraction(firstNumber, secondNumber)
    case "*":
        result = multiplication(firstNumber, secondNumber)
    case "^":
        result = power(firstNumber, secondNumber)
    case _:
        result = "fail"


if result == "fail":
    print("You writed wrong operation")
else:
    print("Result of",firstNumber,operation,secondNumber,"is", result)

