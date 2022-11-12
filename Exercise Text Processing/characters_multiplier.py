first_name, second_name = input().split()
total_sum = 0
if len(first_name) > len(second_name):
    for index in range(len(second_name)):
        first = ord(first_name[index])
        second = ord(second_name[index])
        total_sum += first * second
    for index in range(len(second_name), len(first_name)):
        total_sum += ord(first_name[index])

elif len(second_name) > len(first_name):
    for index in range(len(first_name)):
        first = ord(first_name[index])
        second = ord(second_name[index])
        total_sum += first * second
    for index in range(len(first_name), len(second_name)):
        total_sum += ord(second_name[index])

else:
    for index in range(len(first_name)):
        first = ord(first_name[index])
        second = ord(second_name[index])
        total_sum += first * second

print(total_sum)