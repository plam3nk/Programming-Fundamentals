quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
guineas_weight = float(input())

food_grams = quantity_food * 1000
hay_grams = quantity_hay * 1000
cover_grams = quantity_cover * 1000
weight_grams = guineas_weight * 1000
run_out_of_food = False

for day in range(1, 30 + 1):
    food_grams -= 300

    if day % 2 == 0:
        hay_grams -= food_grams * 0.05
    if day % 3 == 0:
        cover_grams -= weight_grams / 3
    if food_grams <= 0 or hay_grams <= 0 or cover_grams <= 0:
        run_out_of_food = True
        break
food_left_kg = food_grams / 1000
hay_left_kg = hay_grams / 1000
cover_left_kg = cover_grams / 1000
if not run_out_of_food:
    print(f"Everything is fine! Puppy is happy! Food: {food_left_kg:.2f},"
          f" Hay: {hay_left_kg:.2f}, Cover: {cover_left_kg:.2f}.")
else:
    print("Merry must go to the pet store!")
