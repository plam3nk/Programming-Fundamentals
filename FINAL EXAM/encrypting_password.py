import re
result = []
count = int(input())
for line in range(count):
    matched = False
    string = input()
    pattern = r"(^.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|(.{3})<(.+)"
    current_result = re.finditer(pattern, string)
    for match in current_result:
        if match:
            if match.group(1) == match.group(6):
                matched = True
                password = match.group(2) + match.group(3) + match.group(4) + match.group(5)
                print(f"Password: {password}")

    if not matched:
        print("Try another password!")
