def calculator():
    if operator == "multiply":
        result = first_number * second_number
        print(result)
    elif operator == "divide":
        result = int(first_number / second_number)
        print(result)
    elif operator == "add":
        result = first_number + second_number
        print(result)
    elif operator == "subtract":
        result = first_number - second_number
        print(result)


operator = input()
first_number = int(input())
second_number = int(input())

calculator()


