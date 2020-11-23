key = int(input())
number_of_line = int(input())
massage = ''
for i in range(number_of_line):
    symbol = ord(input()) + key
    massage += chr(symbol)
print(massage)