number_of_orders = int(input())

price = 0
total_price = 0
for order in range(number_of_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_capsule < 0.01 or price_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = capsules_per_day * days * price_capsule
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")