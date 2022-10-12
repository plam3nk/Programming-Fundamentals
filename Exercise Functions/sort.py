list_of_numbers_string = input().split()
list_of_numbers = []
for number in list_of_numbers_string:
    current_number = int(number)
    list_of_numbers.append(current_number)
print(sorted(list_of_numbers))