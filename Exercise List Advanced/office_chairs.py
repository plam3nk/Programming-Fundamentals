number_of_rooms = int(input())
game_on = True
chairs_left = 0
for room in range(1, number_of_rooms + 1):
    command = input().split(" ")
    chairs_per_room = len(command[0])
    visitors_per_room = int(command[1])
    chairs_need = visitors_per_room - chairs_per_room
    chairs_left += abs(chairs_need)
    if visitors_per_room > chairs_per_room:
        game_on = False
        chairs_need = visitors_per_room - chairs_per_room
        print(f"{chairs_need} more chairs needed in room {room}")

if game_on:
    print(f"Game On, {chairs_left} free chairs left")

