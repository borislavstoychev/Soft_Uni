n = int(input())
count = n
while count != 0:
    for i in range(n-2):
        if i == 0 or i == n - 3:
            print(chr(43), end='')

        else:
             print(chr(45), end='')

    print()

    count -= 1
