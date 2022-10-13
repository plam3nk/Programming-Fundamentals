tasks = []
sorted_tasks = []
while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("-")
    priority = int(split_command[0])
    current_task = split_command[1]
    tasks.append((priority, current_task))

for action in sorted(tasks):
    sorted_tasks.append(action[1])
print(sorted_tasks)
