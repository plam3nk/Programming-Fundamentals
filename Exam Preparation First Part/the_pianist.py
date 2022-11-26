number_of_pieces = int(input())
collection = {}
for line in range(number_of_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = []
    collection[piece].append(composer)
    collection[piece].append(key)
command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]
    if action == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = []
            collection[piece].append(composer)
            collection[piece].append(key)
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        piece = command[1]
        key = command[2]
        if piece in collection:
            collection[piece][1] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
for piece in collection:
    composer = collection[piece][0]
    key = collection[piece][1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
