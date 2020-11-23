text = input()
encrypted = ""
for i in text:
    encrypted += chr(ord(f"{i}") + 3)
print(encrypted)
