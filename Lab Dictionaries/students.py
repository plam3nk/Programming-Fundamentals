command = input().split(":")
students = {}
while len(command) > 1:
    course = command[2]
    name = command[0]
    id = command[1]
    name_id = f"{name} - {id}"
    if course not in students.keys():
        students[course] = []
        students[course].append(name_id)
    else:
        students[course].append(name_id)

    command = input().split(":")

course_info = command[0]
replaced = course_info.replace("_", " ")
for item in students[replaced]:
    print(item)
