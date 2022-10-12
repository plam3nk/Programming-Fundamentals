numbers_str_list = input().split()
numbers_list = []
for number in numbers_str_list:
    current_number = int(number)
    numbers_list.append(current_number)

print(f"The minimum number is {min(numbers_list)}")
print(f"The maximum number is {max(numbers_list)}")
print(f"The sum number is: {sum(numbers_list)}")