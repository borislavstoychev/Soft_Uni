def fibonacci():

    num = 0
    num1 = 1
    while True:
        yield num
        num1, num = num, num + num1



generator = fibonacci()
for i in range(10):
    print(next(generator))