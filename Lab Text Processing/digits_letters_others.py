characters = input()
letters = ""
numbers = ""
others = ""

for char in characters:
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        letters += char
    elif 48 <= ord(char) <= 57:
        numbers += char
    else:
        others += char

print(numbers)
print(letters)
print(others)
