import re

input_line = input()
pattern = r"(\=[A-Z][A-Za-z][A-Za-z]+\=|\/[A-Z][A-Za-z][A-Za-z]+\/)"

result = re.findall(pattern, input_line)
destinations = []
points = 0
for item in result:
    while "=" in item:
        item = item.replace("=", "")
    while "/" in item:
        item = item.replace("/", "")
    points += len(item)
    destinations.append(item)
print("Destinations: ", end="")
print(", ".join(destinations))
print(f"Travel Points = {points}")