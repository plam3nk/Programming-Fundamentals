phonebook = {}
while True:
    input_line = input()
    if "-" not in input_line:
        break
    name, phone = input_line.split("-")
    phonebook[name] = phone

for search in range(int(input_line)):
    search_name = input()
    if search_name in phonebook.keys():
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")