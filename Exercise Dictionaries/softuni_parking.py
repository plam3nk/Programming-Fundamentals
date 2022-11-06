number_of_commands = int(input())
parking = {}
for line in range(number_of_commands):
    input_line = input().split()
    command = input_line[0]
    name = input_line[1]
    if command == "register":
        license_plate = input_line[2]
        if name not in parking.keys():
            parking[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")

    elif command == "unregister":
        if name not in parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            del parking[name]
            print(f"{name} unregistered successfully")

for item in parking.keys():
    print(f"{item} => {parking[item]}")

