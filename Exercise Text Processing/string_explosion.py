input_line = input()
text = ""
strength = 0
for index in range(len(input_line)):
    if strength > 0 and input_line[index] != ">":
        strength -= 1
    elif input_line[index] == ">":
        text += input_line[index]
        strength += int(input_line[index + 1])
    else:
        text += input_line[index]
print(text)
