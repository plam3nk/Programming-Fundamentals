number_of_lines = int(input())
grades = {}
for line in range(number_of_lines):
    name = input()
    current_grade = float(input())
    if name not in grades.keys():
        grades[name] = []
        grades[name].append(current_grade)
    else:
        grades[name].append(current_grade)

for item in grades.keys():
    average_grade = sum(grades[item]) / len(grades[item])
    grades[item] = average_grade

for student in grades.keys():
    if grades[student] >= 4.50:
        print(f"{student} -> {grades[student]:.2f}")
