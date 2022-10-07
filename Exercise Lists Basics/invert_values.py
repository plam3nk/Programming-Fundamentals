# input_line = input()
# my_list = input_line.split(" ")
# reverted_list = []
# for index in range(len(my_list)):
#     if int(my_list[index]) > 0:
#         reverted_list.append(-abs(int(my_list[index])))
#     elif int(my_list[index]) <= 0:
#         reverted_list.append(abs(int(my_list[index])))
# print(reverted_list)

# ===============
input_line = input()
my_list = input_line.split()
reverted_list = []
for element in my_list:
    number = -int(element)
    reverted_list.append(number)
print(reverted_list)
