def length_validation(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def is_valid(name):
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def redundant_symbols(name):
    if " " in name:
        return False
    return True


usernames = input().split(", ")
for user in usernames:
    if length_validation(user) and is_valid(user) and redundant_symbols(user):
        print(user)
