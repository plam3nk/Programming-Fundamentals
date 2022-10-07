number_of_lines = int(input())
word = input()
lst = []
filtered_list = []
for line in range(number_of_lines):
    current_string = input()
    lst.append(current_string)
    if word in current_string:
        filtered_list.append(current_string)
print(lst)
print(filtered_list)
