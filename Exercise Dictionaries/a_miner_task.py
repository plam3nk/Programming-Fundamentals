command = input()
resources = {}
while command != "stop":
    current_resource = command
    quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = quantity
    else:
        resources[current_resource] += quantity

    command = input()

for item in resources.keys():
    print(f"{item} -> {resources[item]}")