def calculator(product_type, amount_multiplier):
    if product == "coffee":
        return 1.50 * amount
    elif product == "water":
        return 1.00 * amount
    elif product == "coke":
        return 1.40 * amount
    elif product == "snacks":
        return 2.00 * amount


product = input()
amount = int(input())
print(f"{calculator(product, amount):.2f}")

