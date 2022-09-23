input_line = input()

while input_line != "End":
    start = 0
    end = 1
    if input_line == "SoftUni":
        input_line = input()
        continue
    for string in range(len(input_line)):
        print(f"{input_line[start:end:1]}", end='')
        print(f"{input_line[start:end:1]}", end='')
        start += 1
        end += 1
    print()
    input_line = input()
