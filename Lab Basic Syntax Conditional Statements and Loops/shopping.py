budget = int(input())
input_line = input()
total_cost = 0
while input_line != "End":
    price = int(input_line)
    total_cost += price
    if total_cost > budget:
        print("You went in overdraft!")
        break
    input_line = input()
if total_cost <= budget:
    print("You bought everything needed.")
