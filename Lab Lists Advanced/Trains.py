number_of_wagons = int(input())
train = [0] * number_of_wagons
while True:
    input_line = input().split(" ")
    if "End" in input_line:
        break
    command = input_line[0]
    if command == "add":
        people_to_add = int(input_line[1])
        train[-1] += people_to_add
    elif command == "insert":
        index = int(input_line[1])
        people_to_insert = int(input_line[2])
        train[index] += people_to_insert
    elif command == "leave":
        index = int(input_line[1])
        people_to_leave = int(input_line[2])
        train[index] -= people_to_leave
print(train)

