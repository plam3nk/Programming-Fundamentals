number = int(input())
first_chr = 0
for first in range(number):
    first_chr += 1
    second_chr = 0
    for second in range(number):
        second_chr += 1
        third_chr = 0
        for third in range(number):
            third_chr += 1
            print(f"{chr(first_chr + 96)}{chr(second_chr + 96)}{chr(third_chr + 96)}")
