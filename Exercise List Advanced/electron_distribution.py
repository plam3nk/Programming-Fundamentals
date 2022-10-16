number_of_electrons = int(input())
shells = []
left_electrons = number_of_electrons
for shell in range(1, 10):
    shell_size = 2 * shell ** 2
    if shell_size <= left_electrons:
        if left_electrons > 0:
            shells.append(shell_size)
    if shell_size > left_electrons:
        if left_electrons > 0:
            shells.append(left_electrons)
    left_electrons -= shell_size
print(shells)