import re

data = input()
search_pattern = r"\b(\d{2}[-.\/][A-Z][a-z]{2}/\d{4})\b"

result = re.findall(search_pattern, data)
print(result)