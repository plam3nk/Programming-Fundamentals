def rounding_func(number):
    return round(number)


numbers_list = input().split(" ")
rounded_list = []

for num in numbers_list:
    current_number = float(num)
    rounded_list.append(int(rounding_func(current_number)))
print(rounded_list)
