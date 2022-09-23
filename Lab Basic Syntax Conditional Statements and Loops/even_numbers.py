numbers = int(input())

only_even = True
for n in range(numbers):
    current_number = int(input())
    if current_number % 2 != 0:
        only_even = False
        print(f"{current_number} is odd!")
        break
if only_even:
    print("All numbers are even.")