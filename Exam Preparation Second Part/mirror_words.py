import re

input_line = input()
pattern = r"(\@[A-Za-z]{3,}\@)(\@[A-Za-z]{3,}\@)|(\#[A-Za-z]{3,}\#)(\#[A-Za-z]{3,}\#)"
result = re.finditer(pattern, input_line)
matches = []
counter = 0
for item in result:
    counter += 1
    if "#" in item.group():
        match = item.group().split("##")
        first_word = match[0]
        second_word = match[1]
        first_word = first_word.replace("#", "")
        second_word = second_word.replace("#", "")
        if first_word == second_word[::-1]:
            word = f"{first_word} <=> {second_word}"
            matches.append(word)
    elif "@" in item.group():
        match = item.group().split("@@")
        first_word = match[0]
        second_word = match[1]
        first_word = first_word.replace("@", "")
        second_word = second_word.replace("@", "")
        if first_word == second_word[::-1]:
            word = f"{first_word} <=> {second_word}"
            matches.append(word)
if counter == 0:
    print(f"No word pairs found!")
else:
    print(f"{counter} word pairs found!")
if matches:
    print(f"The mirror words are:")
    print(", ".join(matches))
else:
    print(f"No mirror words!")


