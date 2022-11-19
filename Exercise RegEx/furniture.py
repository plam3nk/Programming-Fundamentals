import re

line = input()
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
bought_furniture = []
cost = 0
while line != "Purchase":
    match = re.search(pattern, line)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        cost += float(price) * int(quantity)
    line = input()
print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {cost:.2f}")
