library = input().split("&")

while True:
    commands = input()
    if commands == "Done":
        break
    command = commands.split(" | ")[0]
    if command == "Add Book":
        book = commands.split(" | ")[1]
        if book not in library:
            library.insert(0, book)
    elif command == "Take Book":
        book = commands.split(" | ")[1]
        if book in library:
            library.remove(book)
    elif command == "Swap Books":
        book1 = commands.split(" | ")[1]
        book2 = commands.split(" | ")[2]
        if book1 in library and book2 in library:
            index_book1 = library.index(book1)
            index_book2 = library.index(book2)
            library[index_book1] = book2
            library[index_book2] = book1
    elif command == "Insert Book":
        book = commands.split(" | ")[1]
        library.append(book)
    elif command == "Check Book":
        index = commands.split(" | ")[1]
        index  = int(index)
        if index < len(library):
            print(library[index])

print(", ".join(library))