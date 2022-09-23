number = int(input())
for i in range(1, number + 1):
    for stars_up in range(0, i):
        print("*", end='')
    print()
for j in range(number - 1, 0, -1):
    for stars_down in range(0, j):
        print("*", end='')
    print()
