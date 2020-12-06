import sys
from math import floor
num_of_flight = int(input())
max_passengers = -sys.maxsize
max_name = ''
for i in range(num_of_flight):
    name = input()
    line = input()
    count = 0
    passenger = 0
    while line != 'Finish':
        passenger += int(line)
        count += 1
        line = input()
    avr_passengers = passenger / count
    if avr_passengers > max_passengers:
        max_passengers = avr_passengers
        max_name = name
    print(f'{name}: {floor(avr_passengers)} passengers.')
print(f"{max_name} has most passengers per flight: {floor(max_passengers)}")