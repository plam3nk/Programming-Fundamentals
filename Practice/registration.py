username = input()
command = input()
while command != "Registration":
    command = command.split()
    action = command[0]
    if action == "Letters":
        condition = command[1]
        if condition == "Lower":
            username = username.lower()
            print(username)
        elif condition == "Upper":
            username = username.upper()
            print(username)
    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(username) and 0 <= end_index <= len(username):
            substring = username[start_index:end_index+1]
            reversed_substring = substring[::-1]
            print(reversed_substring)
    elif action == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif action == "Replace":
        character = command[1]
        if character in username:
            username = username.replace(character, "-")
            print(username)
    elif action == "IsValid":
        character = command[1]
        if character in username:
            print("Valid username.")
        else:
            print(f"{character} must be contained in your username.")

    command = input()
