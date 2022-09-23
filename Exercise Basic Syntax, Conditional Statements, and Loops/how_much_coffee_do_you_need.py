command = input()
coffee_counter = 0
while command != "END":
    if coffee_counter > 5:
        break
    if command == "coding" or \
        command == "dog" or \
        command == "cat" or \
            command == "movie":
        coffee_counter += 1
    if command == "CODING" or \
        command == "DOG" or \
        command == "CAT" or \
            command == "MOVIE":
        coffee_counter += 2
    command = input()
if coffee_counter < 6:
    print(f"{coffee_counter}")
else:
    print(f"You need extra sleep")
