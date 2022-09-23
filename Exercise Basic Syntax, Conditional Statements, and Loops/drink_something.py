age = int(input())

drink_type = 0
if age <= 14:
    drink_type = "toddy"
elif age <= 18:
    drink_type = "coke"
elif age <= 21:
    drink_type = "beer"
elif age > 21:
    drink_type = "whisky"
print(f"drink {drink_type}")
