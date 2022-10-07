string_of_integers = input()
my_list = string_of_integers.split(",")
beggars = int(input())
new_list = []
result = 0
for beggar in range(1, beggars + 1):
    result = 0
    for index in range(beggar - 1, len(my_list), beggars):
        result += int(my_list[index])
    new_list.append(result)
print(new_list)