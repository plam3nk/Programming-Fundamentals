factor = int(input())
count = int(input())
length = factor * count
my_list = []
for number in range(factor, length + 1, factor):
    my_list.append(number)
print(my_list)