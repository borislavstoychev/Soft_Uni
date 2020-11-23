n = int(input())
count = 0
for i in range(n):
    letter = input()
    count += ord(letter)
print(f"The sum equals: {count}")
