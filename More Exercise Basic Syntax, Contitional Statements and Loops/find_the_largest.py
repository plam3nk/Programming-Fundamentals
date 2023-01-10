number = input()
digit_list = []
for digit in number:
    current_digit = digit
    digit_list.append(current_digit)

digit_list = sorted(digit_list, reverse=True)
biggest_number = ""
for digit in digit_list:
    biggest_number += digit
print(biggest_number)