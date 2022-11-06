courses = {}
input_line = input()
while input_line != "end":
    course_name, student_name = input_line.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
        courses[course_name].append(student_name)
    else:
        courses[course_name].append(student_name)

    input_line = input()

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
