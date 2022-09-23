year = int(input())
current_year = year
is_special = False
while not is_special:
    current_year += 1
    happy_year_set = set()
    string_current_year = str(current_year)
    for digit in string_current_year:
        happy_year_set.add(digit)
    if len(happy_year_set) == len(string_current_year):
        is_special = True
        print(f"{current_year}")

