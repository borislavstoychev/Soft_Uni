try:
    with open("text.txt") as file:
        print("Fail found")
except FileNotFoundError:
    print("File not found")