string_list = input().split()
for word in string_list:
    current_print = word * len(word)
    print(current_print, end="")