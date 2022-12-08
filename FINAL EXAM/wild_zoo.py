command = input()
animals = {}
while command != "EndDay":
    command = command.split(": ")
    action = command[0]
    info = command[1]
    info = info.split("-")
    if action == "Add":
        animal_name = info[0]
        needed_food = int(info[1])
        area = info[2]
        if animal_name in animals:
            animals[animal_name][0] += needed_food
            animals[animal_name][1] = area
        else:
            animals[animal_name] = []
            animals[animal_name].append(needed_food)
            animals[animal_name].append(area)
    if action == "Feed":
        animal_name = info[0]
        food = int(info[1])
        if animal_name in animals:
            animals[animal_name][0] -= food
            if animals[animal_name][0] <= 0:
                print(f"{animal_name} was successfully fed")
                del animals[animal_name]

    command = input()

areas = {}
for animal in animals:
    if animals[animal][1] not in areas:
        areas[animals[animal][1]] = 1
    else:
        areas[animals[animal][1]] += 1
print(f"Animals:")
for animal in animals:
    print(f" {animal} -> {animals[animal][0]}g")
print("Areas with hungry animals:")
for area in areas:
    print(f" {area}: {areas[area]}")

