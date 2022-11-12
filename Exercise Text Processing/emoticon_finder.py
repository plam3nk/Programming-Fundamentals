message = input()
for index in range(len(message)):
    if message[index] == ":":
        emoticon = message[index] + message[index + 1]
        print(emoticon)