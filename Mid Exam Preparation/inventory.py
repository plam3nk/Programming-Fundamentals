items = input().split(", ")
command = input().split(" - ")
while not "Craft!" in command:
    action = command[0]
    current_item = command[1]
    if action == "Collect":
        if current_item in items:
            command = input().split(" - ")
            continue
        items.append(current_item)
    elif action == "Drop":
        if current_item in items:
            items.remove(current_item)
    elif action == "Combine Items":
        current_items = current_item.split(":")
        old_item = current_items[0]
        new_item = current_items[1]
        for index in range(len(items)):
            if items[index] == old_item:
                items.insert(index + 1, new_item)
    elif action == "Renew":
        if current_item in items:
            for i in range(len(items)):
                if current_item == items[i]:
                    items.remove(current_item)
                    items.append(current_item)
    command = input().split(" - ")
print(", ".join(items))
