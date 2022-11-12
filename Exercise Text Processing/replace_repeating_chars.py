input_line = input()
message = input_line[0]
for character in input_line:
    if message[-1] != character:
        message += character

print(message)
