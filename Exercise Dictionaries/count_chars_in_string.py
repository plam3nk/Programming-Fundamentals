word = input()
letters_count = {}
for character in word:
    if character != " ":
        value = word.count(character)
        key = character
        letters_count[key] = value

for key in letters_count.keys():
    print(f"{key} -> {letters_count[key]}")
