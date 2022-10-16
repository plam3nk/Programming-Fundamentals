words_list = input().split()
filtered_words = [word for word in words_list if len(word) % 2 == 0]
for word in filtered_words:
    print(word)