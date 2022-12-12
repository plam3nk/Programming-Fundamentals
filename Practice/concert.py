command = input()
concert = {}
band_times = {}
while command != "Start!":
    command = command.split("; ")
    action = command[0]
    if action == "Add":
        band = command[1]
        names = command[2].split(", ")
        if band not in concert:
            concert[band] = names
        else:
            for name in names:
                if name not in concert[band]:
                    concert[band].append(name)
    elif action == "Play":
        band = command[1]
        time = int(command[2])
        if band not in concert:
            concert[band] = []
        if band not in band_times:
            band_times[band] = time
        elif band in band_times:
            band_times[band] += time
    command = input()

total_time = 0
for band in band_times:
    current_time = band_times[band]
    total_time += current_time
print(f"Total time: {total_time}")
for band in band_times:
    print(f"{band} -> {band_times[band]}")
for band in concert:
    print(band)
    for name in concert[band]:
        print(f"=> {name}")
    break

