import random
computer_number = random.randint(1, 100)
is_guessed = False
while not is_guessed:
    player_number = input("Guess the number(1-100): ")
    if not player_number.isdigit():
        print("Invalid input. Try again...")
        continue
    if int(player_number) == computer_number:
        print("You guess it!")
        is_guessed = True
    elif int(player_number) > computer_number:
        print("Too high!")
    elif int(player_number) < computer_number:
        print("Too low!")