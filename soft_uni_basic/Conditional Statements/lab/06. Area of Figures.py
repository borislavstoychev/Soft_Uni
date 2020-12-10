shape = input()
area = 0.0
import math
if shape == "square":
    side = float(input())
    area = side * side
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif shape == "circle":
    side_r = float(input())
    area = side_r * side_r * math.pi
elif shape == 'triangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b / 2
print(area)