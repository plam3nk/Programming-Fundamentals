stops = input()

command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if len(stops) >= index:
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2]) + 1
        if len(stops) >= start_index and len(stops) >= end_index:
            stops = stops[0:start_index] + stops[end_index:]
        print(stops)
    elif action == "Switch":
        old_string = command[1]
        replacement = command[2]
        stops = stops.replace(old_string, replacement)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
