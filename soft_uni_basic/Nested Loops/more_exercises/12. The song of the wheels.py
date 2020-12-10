m = int(input())
password = False
count = 0
output = ''
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and (a * b) + (c * d) == m:
                    count += 1
                    print(f'{a}{b}{c}{d}', end=' ')
                    if count == 4:
                        password = True
                        output = f'Password: {a}{b}{c}{d}'
print()
if password:
    print(output)
else:
    print('No!')



