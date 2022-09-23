lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_brakes = 0
for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        expenses += helmet_price
        if fight % 3 == 0:
            expenses += sword_price
            expenses += shield_price
            shield_brakes += 1
    elif fight % 3 == 0:
        expenses += sword_price
    if shield_brakes == 2:
        expenses += armor_price
        shield_brakes = 0
print(f"Gladiator expenses: {expenses:.2f} aureus")