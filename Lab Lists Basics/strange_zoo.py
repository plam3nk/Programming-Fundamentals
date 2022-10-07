head = input()
body = input()
tail = input()

part_list = [head, body, tail]
part_list[0], part_list[2] = part_list[2], part_list[0]
print(part_list)