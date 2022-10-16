numbers_list = [int(number) for number in input().split(", ")]
positive_list = [p_number for p_number in numbers_list if p_number >= 0]
negative_list = [n_number for n_number in numbers_list if n_number < 0]
even_list = [e_number for e_number in numbers_list if e_number % 2 == 0]
odd_list = [e_number for e_number in numbers_list if e_number % 2 != 0]
print("Positive:", end=" "), print(*positive_list, sep=", ")
print("Negative:", end=" "), print(*negative_list, sep=", ")
print("Even:", end=" "), print(*even_list, sep=", ")
print("Odd:", end=" "), print(*odd_list, sep=", ")
