
def perform_addition(num1=0,num2=0):
    return num1 + num2

def perform_subtraction(num1=0,num2=0):
    if (num1 - num2) < 0:
        return num2 - num1
    return num1 - num2

def perform_mulitiplication(num1=0,num2=0):
    return num1 * num2

def perform_division(num1=0,num2=0):
    return num1 / num2


first_number = int(input("Enter first number here: "))
operation = input("Enter opertaion +,-,x or / : ")
second_number = int(input("Enter second number: "))

if "+" in operation:
    print("Answer is ",perform_addition(first_number,second_number))
elif "-" in operation:
    print("Answer is ",perform_subtraction(first_number,second_number))
elif "x" in operation:
    print("Answer is ",perform_mulitiplication(first_number,second_number))
elif "/" in operation:
    print("Answer is ",perform_division(first_number,second_number))
else:
    print("Invalid operation please enter + or - or x or /")
    

