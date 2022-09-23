tank_capacity = 255
number_of_lines = int(input())
poured_water = 0
for line in range(number_of_lines):
    water = int(input())
    poured_water += water
    if poured_water > tank_capacity:
        poured_water -= water
        print("Insufficient capacity!")
print(poured_water)