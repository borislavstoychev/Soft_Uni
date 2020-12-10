length = int(input())
width = int(input())
height = int(input())
volume = float(input()) / 100
liters = length * width * height * 0.001
liters_that_we_need = liters - (liters * volume)
print(liters_that_we_need)