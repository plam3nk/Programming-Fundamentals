command = input()
is_not_found = True
while command != "Welcome!":
    name = command
    if name == "Voldemort":
        is_not_found = False
        print("You must not speak of that name!")
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    command = input()
if is_not_found:
    print("Welcome to Hogwarts.")