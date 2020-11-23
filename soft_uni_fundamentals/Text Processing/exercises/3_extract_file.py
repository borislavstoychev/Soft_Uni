file_name = input().split("\\")
name, extension = "".join(file_name[:-2:-1]).split(".")
print(f"File name: {name}\nFile extension: {extension}")

