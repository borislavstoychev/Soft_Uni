chat_logger = []
while True:
    commands = input()
    if commands == "end":
        break
    command = commands.split()[0]
    if command == "Chat":
        message = commands.split()[1]
        chat_logger.append(message)
    elif command == "Delete":
        message_to_delete = commands.split()[1]
        if message_to_delete in chat_logger:
            chat_logger.remove(message_to_delete)
    elif command == "Edit":
        message_to_edit = commands.split()[1]
        edited_version = commands.split()[2]
        if message_to_edit in chat_logger:
            index = chat_logger.index(message_to_edit)
            chat_logger[index] = edited_version
    elif command == "Pin":
        message_to_pin = commands.split()[1]
        if message_to_pin in chat_logger:
            chat_logger.remove(message_to_pin)
            chat_logger.append(message_to_pin)
    elif command == "Spam":
        for i in range(len(commands.split())):
            if not i == 0:
                message_n = commands.split()[i]
                chat_logger.append(message_n)

print("\n".join(chat_logger))
