numbers = input()
count = int(input())
numbers_list = numbers.split(" ")
integer_list = []
for index in range(len(numbers_list)):
    integer_list.append(int(numbers_list[index]))
integer_list.sort(reverse=True)
length = int(len(integer_list)) - count
for second_index in range(length, len(integer_list)):
    if str(integer_list[second_index]) in numbers_list:
        numbers_list.remove((str(integer_list[second_index])))
print(*numbers_list, sep=", ")