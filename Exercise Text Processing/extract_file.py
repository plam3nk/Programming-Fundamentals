path = input().split("\\")
file_name, type_of_file = path[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {type_of_file}")