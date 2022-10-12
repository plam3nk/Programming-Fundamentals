def characters_in_range(first_char, second_char):
    list_of_characters = []
    for character in range(ord(first_char) + 1, ord(second_char)):
        list_of_characters.append(chr(character))
    return list_of_characters


first_character = input()
second_character = input()
result = characters_in_range(first_character, second_character)
print(' '.join(result))
