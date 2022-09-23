group_size = int(input())
days = int(input())
coins = 0
total_coins = 0
for day in range(1, days + 1):
    coins = 0
    coins += 50
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2
    coins -= group_size * 2
    if day % 3 == 0:
        coins -= group_size * 3
    if day % 5 == 0:
        coins += group_size * 20
        if day % 3 == 0:
            coins -= group_size * 2
    total_coins += coins
coins_per_companion = total_coins / group_size
print(f"{group_size} companions received {int(coins_per_companion)} coins each.")