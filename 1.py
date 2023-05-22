def valuesAvailable():
    print("here is the list of options you have")
    print("a - Addition")
    print("b - Subtraction")
    print("c - multiplication")
    print("d - division")
    print("e - exit")
    return str(input("Choose one option: "))
operandva = valuesAvailable()
if operandva == "a":
    numberOne = int(input("enter first number: "))
    numberTwo = int(input("enter second number: "))
    print(numberOne+numberTwo)

elif operandva == "b":
    numberOne = int(input("enter first number: "))
    numberTwo = int(input("enter second number: "))
    print(numberOne-numberTwo)

elif operandva == "c":
    numberOne = int(input("enter first number: "))
    numberTwo = int(input("enter second number: "))
    print(numberOne*numberTwo)

elif operandva == "d":
    numberOne = int(input("enter first number: "))
    numberTwo = int(input("enter second number: "))
    print(numberOne/numberTwo)

elif operandva == "e" :
    print("you have exited successfully") 

else:
    valuesAvailable() 