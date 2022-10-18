sequence_of_number = [int(number) for number in input().split(", ")]
highest_number = max(sequence_of_number)
max_group = highest_number
current_group = 0
current_list = []
while max_group % 10 != 0:
    max_group += 1
while current_group != max_group:
    current_group += 10
    for num in sequence_of_number:
        if num <= current_group:
            current_list.append(num)
    print(f"Group of {current_group}'s: {current_list}")
    for num in current_list:
        if num in sequence_of_number:
            sequence_of_number.remove(num)
    current_list.clear()


