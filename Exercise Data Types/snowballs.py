snowballs_made = int(input())
highest_value = 0
highest_weight = 0
quickest_time = 0
highest_quality = 0
for snowball in range(snowballs_made):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality
    if value > highest_value:
        highest_value = value
        highest_weight = snowball_weight
        quickest_time = snowball_time
        highest_quality = snowball_quality
print(f"{highest_weight} : {quickest_time} = {int(highest_value)} ({highest_quality})")



