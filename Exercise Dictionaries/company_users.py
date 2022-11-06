command = input()
company_users = {}
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_users.keys():
        company_users[company_name] = []
        company_users[company_name].append(employee_id)
    else:
        if employee_id not in company_users[company_name]:
            company_users[company_name].append(employee_id)

    command = input()

for company in company_users.keys():
    print(f"{company}")
    for employee in company_users[company]:
        print(f"-- {employee}")