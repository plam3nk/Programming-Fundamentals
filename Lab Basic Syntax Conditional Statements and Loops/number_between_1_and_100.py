is_found = False
is_not_found = True
while is_not_found:
    number = float(input())
    if 1 <= number <= 100:
        is_not_found = False
        is_found = True
        break
if is_found:
    print(f"The number {number} is between 1 and 100")


