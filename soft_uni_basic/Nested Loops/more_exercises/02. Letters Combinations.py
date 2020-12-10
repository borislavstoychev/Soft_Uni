beginning = input()
end = input()
not_incl = input()
count = 0
for a in range(ord(beginning), ord(end) + 1):
    for b in range(ord(beginning), ord(end) + 1):
        for c in range(ord(beginning), ord(end) + 1):
            if chr(a) != not_incl and chr(b) != not_incl and chr(c) != not_incl:
                count += 1
                print(f'{chr(a)}{chr(b)}{chr(c)}', end=' ')
print(count)