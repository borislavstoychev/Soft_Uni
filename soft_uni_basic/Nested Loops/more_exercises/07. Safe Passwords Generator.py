a = int(input())
b = int(input())
max_passcod = int(input())
num_of_passcod = 0
stop = False
for c in range(35, 55):
    if stop:
        break
    for d in range(64, 96):
        if stop:
            break
        for e in range(1, a + 1):
            if stop:
                break
            for f in range(1, b + 1):
                if stop:
                    break
                print(f"{chr(c)}{chr(d)}{e}{f}{chr(d)}{chr(c)}{chr(124)}", end='')
                num_of_passcod += 1
                c += 1
                if c > 55:
                    c = 35
                d += 1
                if d > 96:
                    d = 64
                if num_of_passcod == max_passcod or (e == a and f == b):
                    stop = True
                    break



