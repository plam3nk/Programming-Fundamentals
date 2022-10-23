coffee_list = input().split(" ")
commands_count = int(input())

for command in range(commands_count):
    current_command = input().split(" ")
    action = current_command[0]
    if action == "Include":
        coffee = current_command[1]
        coffee_list.append(coffee)
    elif action == "Remove":
        order = current_command[1]
        amount = int(current_command[2])
        counter = 0
        if order == "last":
            for first_index in range(len(coffee_list) - 1, 0, -1):
                if amount >= len(coffee_list):
                    break
                if amount == counter:
                    break
                else:
                    coffee_list[first_index] = "none"
                    counter += 1
            while "none" in coffee_list:
                coffee_list.remove("none")
        elif order == "first":
            for second_index in range(len(coffee_list)):
                if amount >= len(coffee_list):
                    break
                if amount == counter:
                    break
                else:
                    coffee_list[second_index] = "none"
                    counter += 1
            while "none" in coffee_list:
                coffee_list.remove("none")
    elif action == "Prefer":
        index_one = int(current_command[1])
        index_two = int(current_command[2])
        if index_one < len(coffee_list) and index_two < len(coffee_list):
            coffee_list[index_one], coffee_list[index_two] = coffee_list[index_two], coffee_list[index_one]
    elif action == "Reverse":
        coffee_list.reverse()
print("Coffees:")
print(" ".join(coffee_list))