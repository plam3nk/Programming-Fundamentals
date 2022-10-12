def odd_and_even_sum(number):  # sum of odd numbers in number and even numbers in number
    odd_sum = 0
    even_sum = 0
    for digit in number:
        current_digit = int(digit)
        if current_digit % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit
    return odd_sum, even_sum


input_number = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(input_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
