from math import ceil

budget = float(input())
students = int(input())
flour_package_price = float(input())
egg_price = float(input())
apron_price = float(input())

free_flour = students // 5
amount_flour = students - free_flour
amount_eggs = students * 10
amount_aprons = ceil(students * 1.20)

cost = amount_flour * flour_package_price + amount_eggs * egg_price + amount_aprons * apron_price
diff = cost - budget
if budget >= cost:
    print(f"Items purchased for {cost:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")