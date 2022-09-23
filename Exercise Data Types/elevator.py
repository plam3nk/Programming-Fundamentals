persons_to_elevate = int(input())
capacity_of_elevator = int(input())

courses = persons_to_elevate // capacity_of_elevator
left_to_elevate = persons_to_elevate % capacity_of_elevator
if left_to_elevate > 0:
    courses += 1
print(courses)