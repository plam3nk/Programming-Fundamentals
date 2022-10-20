list_targets = [int(number) for number in input().split(" ")]
command = input()
shot_targets = []
while command != "End":
    current_target = int(command)
    if len(list_targets) - 1 < current_target:
        command = input()
        continue
    target_value = list_targets[current_target]
    if current_target <= len(list_targets):
        list_targets[current_target] = -1
        shot_targets.append(list_targets[current_target])
        for index in range(len(list_targets)):
            if list_targets[index] in shot_targets:
                continue
            elif list_targets[index] <= target_value:
                list_targets[index] += target_value
            elif list_targets[index] > target_value:
                list_targets[index] -= target_value
    command = input()
list_targets_string = [str(num) for num in list_targets]
print(f"Shot targets: {len(shot_targets)} ->", end=" ")
print(" ".join(list_targets_string))
