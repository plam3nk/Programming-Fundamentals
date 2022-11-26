number_of_heroes = int(input())
heroes = {}
for line in range(number_of_heroes):
    hero, hp, mp = input().split(" ")
    heroes[hero] = []
    heroes[hero].append(int(hp))
    heroes[hero].append(int(mp))

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero][1] >= mp_needed:
            heroes[hero][1] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        if heroes[hero][0] > damage:
            heroes[hero][0] -= damage
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]
    elif action == "Recharge":
        hero = command[1]
        amount = int(command[2])
        heroes[hero][1] += amount
        if heroes[hero][1] > 200:
            diff = heroes[hero][1] - 200
            amount -= diff
            heroes[hero][1] = 200
        print(f"{hero} recharged for {amount} MP!")
    elif action == "Heal":
        hero = command[1]
        amount = int(command[2])
        heroes[hero][0] += amount
        if heroes[hero][0] > 100:
            diff = heroes[hero][0] - 100
            amount -= diff
            heroes[hero][0] = 100
        print(f"{hero} healed for {amount} HP!")

    command = input()
for hero in heroes:
    print(hero)
    print(f"    HP: {heroes[hero][0]}")
    print(f"    MP: {heroes[hero][1]}")
