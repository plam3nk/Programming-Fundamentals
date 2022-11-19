import re

text = input()
while text:
    pattern = r"www.[A-Za-z\d\-]+\.[\.A-Za-z]+"
    match = re.findall(pattern, text)
    if match:
        print(" ".join(match))
    text = input()