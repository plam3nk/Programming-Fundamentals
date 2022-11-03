command = input()
products = {}
while command != "statistics":
    split_command = command.split(": ")
    key = split_command[0]
    value = int(split_command[1])
    if key in products.keys():
        products[key] += value
    else:
        products[key] = value

    command = input()
print("Products in stock:")
key_counter = 0
value_sum = 0
for key in products.keys():
    key_counter += 1
    value_sum += int(products[key])
    print(f"- {key}: {products[key]}")
print(f"Total Products: {key_counter}")
print(f"Total Quantity: {value_sum}")