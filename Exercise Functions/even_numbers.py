def even_numbers(number):
    if number % 2 == 0:
        return True
    else:
        return False


list_of_numbers_string = input().split(" ")
list_of_numbers = []
for number in list_of_numbers_string:
    current_number = int(number)
    list_of_numbers.append(current_number)

even_list = list(filter(even_numbers, list_of_numbers))
print(even_list)
