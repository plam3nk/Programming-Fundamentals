characters_list = input().split(", ")
ascii_values = {key: ord(key) for key in characters_list}
print(ascii_values)