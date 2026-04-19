import art
print(art.logo)


def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

operations = {
    "+": add ,
    "-": subtract ,
    "*": multiply ,
    "/": divide
}
def calculator():
    should_accumulate = True
    first_number= int(input("What is the first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        selected_operation= input("Pick an operation:")
        second_number= int(input("What is the next number?"))

        answer= operations[selected_operation](first_number, second_number)
        print(f"{first_number} {selected_operation} {second_number} = {answer}")
        choice = input(f"Type 'y' to continue with the previous result {answer}, or type 'n' to start a new calculation.")
        if choice == "y":
            first_number= answer
        else:
            should_accumulate= False
            print("\n" * 20)
            calculator()

calculator()
