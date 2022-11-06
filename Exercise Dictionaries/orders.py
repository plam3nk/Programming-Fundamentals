input_line = input()
products = {}
while input_line != "buy":
    key, price, quantity = input_line.split()
    price = float(price)
    quantity = int(quantity)
    value = [quantity, price]
    if key not in products.keys():
        products[key] = [quantity, price]
    else:
        products[key][0] += quantity
        products[key][1] = price

    input_line = input()

for item in products.keys():
    products[item] = products[item][0] * products[item][1]
    print(f"{item} -> {products[item]:.2f}")