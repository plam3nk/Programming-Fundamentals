number_of_lines = int(input())
numbers_list = []
for line in range(number_of_lines):
    current_number = int(input())
    numbers_list.append(current_number)
command = input()
number = 0
filtered_list = []
for index in range(len(numbers_list)):
    if command == "even" and int(numbers_list[index]) % 2 == 0:
        filtered_list.append(numbers_list[index])
    elif command == "odd" and int(numbers_list[index]) % 2 != 0:
        filtered_list.append(numbers_list[index])
    elif command == "positive" and int(numbers_list[index]) >= 0:
        filtered_list.append(numbers_list[index])
    elif command == "negative" and int(numbers_list[index]) < 0:
        filtered_list.append(numbers_list[index])
print(filtered_list)

