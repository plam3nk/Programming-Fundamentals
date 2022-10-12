def factorial_division(first, second):
    first_factorial = 1
    second_factorial = 1
    for digit_first in range(first, 1, -1):
        first_factorial *= digit_first
    for digit_second in range(second, 1, -1):
        second_factorial *= digit_second
    result = first_factorial / second_factorial
    return result


first_number = int(input())
second_number = int(input())
factorial = factorial_division(first_number, second_number)
print(f"{factorial:.2f}")