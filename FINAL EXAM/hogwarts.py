spell = input()
command = input()
while command != "Abracadabra":
    command = command.split()
    action = command[0]
    if action == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif action == "Illusion":
        index = int(command[1])
        letter = command[2]
        if len(spell) > index:
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        substring = command[1]
        replacement = command[2]
        if substring in spell:
            spell = spell.replace(substring, replacement)
            print(spell)
    elif action == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")

    command = input()
