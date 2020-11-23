num = int(input())

for a in range(2, num):
    if num % a == 0:
        print(False)
        break
    else:
        print(True)
        break
