words_count = int(input())
words_dict = {}
for item in range(words_count):
    word = input()
    synonym = input()
    if word not in words_dict.keys():
        words_dict[word] = []
        words_dict[word].append(synonym)
    else:
        words_dict[word].append(synonym)

for key in words_dict.keys():
    print(f"{key} - {', '.join(words_dict[key])}")
