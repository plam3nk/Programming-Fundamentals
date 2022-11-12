message = input()
encrypted_message = ""
for character in message:
    encrypted_char = ord(character) + 3
    encrypted_message += chr(encrypted_char)
print(encrypted_message)