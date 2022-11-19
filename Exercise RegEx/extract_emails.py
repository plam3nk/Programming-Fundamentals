import re

text = input()
pattern = r"\b[A-Za-z0-9\-\.\_]+@[a-z\.\\-]+\b"
matches = re.findall(pattern, text)
print(matches)