import re

lines = int(input())
registrations_counter = 0
for line in range(lines):
    input_line = input()
    pattern = r"U\$([A-Z][a-z]{2,})U\$P\@\$([A-Za-z]{5,}\d{1,})P\@\$"
    result = re.finditer(pattern, input_line)
    invalid = True
    for match in result:
        username = match.group(1)
        password = match.group(2)
        if username and password:
            invalid = False
            print(f"Registration was successful")
            print(f"Username: {username}, Password: {password}")
            registrations_counter += 1
            break
    if invalid:
        print("Invalid username or password")
print(f"Successful registrations: {registrations_counter}")
