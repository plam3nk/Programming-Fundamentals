list_of_materials = input().split()
obtained = False
materials = {"shards": 0, "fragments": 0, "motes": 0}
while not obtained:
    for index in range(0, len(list_of_materials), 2):
        quantity = int(list_of_materials[index])
        key = list_of_materials[index + 1].lower()
        if key not in materials.keys():
            materials[key] = quantity
        else:
            materials[key] += quantity
        if materials[key] >= 250:
            if key == "shards":
                print(f"Shadowmourne obtained!")
                materials[key] -= 250
                obtained = True
            elif key == "fragments":
                print(f"Valanyr obtained!")
                materials[key] -= 250
                obtained = True
            elif key == "motes":
                print(f"Dragonwrath obtained!")
                materials[key] -= 250
                obtained = True
        if obtained:
            break
    if obtained:
        break
    list_of_materials = input().split()

for item in materials.keys():
    print(f"{item}: {materials[item]}")
