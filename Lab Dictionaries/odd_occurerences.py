words_list = input().split(" ")
words_lower = [word.lower() for word in words_list]
result = {}
for item in words_lower:
    word_counter = words_lower.count(item)
    if word_counter % 2 != 0:
        result[item] = item

for value in result.values():
    print(value, end=" ")