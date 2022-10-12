def perfect_number(number):
    divisors_sum = 0
    for num in range(1, number):
        if number % num == 0:
            divisors_sum += num
    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


input_number = int(input())
print(perfect_number(input_number))