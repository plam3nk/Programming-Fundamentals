number = int(input())
is_special = False
for current_number in range(1, number + 1):
    is_special = False
    string_of_current_number = str(current_number)
    digit_sum = 0
    for digit in string_of_current_number:
        digit_sum += int(digit)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
