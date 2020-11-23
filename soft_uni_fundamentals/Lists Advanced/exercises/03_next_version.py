version = input().split(".")

new_version = int("".join(version)) + 1
new_version = list(str(new_version))
new_version = ".".join(new_version)

print(new_version)
