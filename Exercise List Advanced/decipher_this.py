secret_message = input().split()
message = []
numbers_in_word_splitted = []
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for word in range(len(secret_message)):
    current_word = []
    for character in secret_message[word]:
        current_word.append(character)
    for character in current_word:
        if character in numbers:
            numbers_in_word_splitted.append(character)
    for num in numbers:
        while num in current_word:
            current_word.remove(num)

    numbers_in_word = ["".join(numbers_in_word_splitted)]

    first_letter = chr(int(numbers_in_word[0]))
    current_word.insert(0, first_letter)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    current_message = ("".join(current_word))
    message.append(current_message)

    numbers_in_word.clear()
    numbers_in_word_splitted.clear()
print(*message)
