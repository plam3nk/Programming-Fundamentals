string_numbers = list(map(int, input().split(", ")))
found_indices = map(lambda x: x if string_numbers[x] % 2 == 0 else 'no', range(len(string_numbers)))
even_indices = list(filter(lambda a: a != 'no', found_indices))
print(even_indices)