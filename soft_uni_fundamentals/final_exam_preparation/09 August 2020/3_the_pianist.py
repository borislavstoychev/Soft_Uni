n = int(input())
pieces = {}
for _ in range(n):
    piece, composer, key = input().split("|")
    if composer not in pieces:
        pieces[piece] = [composer, key]
commands = input()
while not commands == "Stop":
    command = commands.split("|")[0]
    if command == "Add":
        piece, composer, key = commands.split("|")[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        piece = commands.split("|")[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        piece, new_key = commands.split("|")[1:]
        if piece in pieces:
            print(f"Changed the key of {piece} to {new_key}!")
            pieces[piece][1] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    commands = input()
for (key, value) in dict(sorted(pieces.items(), key=lambda el: (el[0], el[1][0]))).items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")