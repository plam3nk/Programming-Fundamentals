chat = []
command = input()
while command != "end":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Chat":
        message = current_command[1]
        chat.append(message)
    elif action == "Delete":
        message = current_command[1]
        if message in chat:
            chat.remove(message)
    elif action == "Edit":
        old_message = current_command[1]
        edited_version = current_command[2]
        for index in range(len(chat)):
            if chat[index] == old_message:
                chat[index] = edited_version
    elif action == "Pin":
        message = current_command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif action == "Spam":
        messages = current_command
        for index in range(1, len(messages)):
            current_message = messages[index]
            chat.append(current_message)

    command = input()
for item in chat:
    print(item)