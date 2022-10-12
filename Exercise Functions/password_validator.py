def password_validator(password):
    digit_counter = 0
    length = False
    only_letters_digits = False
    two_digits = False
    if 6 <= len(password) <= 10:
        length = True
    for element in password:
        if 48 <= ord(element) <= 57 or\
            97 <= ord(element) <= 122 or\
                65 <= ord(element) <= 90:
            only_letters_digits = True
        else:
            only_letters_digits = False
            break
        if 48 <= ord(element) <= 57:
            digit_counter += 1
    if digit_counter >= 2:
        two_digits = True
    if length and only_letters_digits and two_digits:
        print("Password is valid")
    if not length:
        print("Password must be between 6 and 10 characters")
    if not only_letters_digits:
        print("Password must consist only of letters and digits")
    if not two_digits:
        print("Password must have at least 2 digits")


password_input = input()
password_validator(password_input)
