from math import floor
x_square_meters = int(input())
y_grapes_for_1sq_meters = float(input())
z_wine_needed_liters = int(input())
num_of_worker = int(input())

wine_graps = (x_square_meters * y_grapes_for_1sq_meters*0.4/2.5)
if wine_graps < z_wine_needed_liters:
    print(f'It will be a tough winter! More {floor(z_wine_needed_liters - wine_graps)} liters wine needed.')
else:
    rest_wine = (wine_graps - z_wine_needed_liters)
    wine_per_worker = (rest_wine / num_of_worker)
    print(f'Good harvest this year! Total wine: {floor(wine_graps)} liters.')
    print(f'{floor(rest_wine)} liters left -> {floor(wine_per_worker)} liters per person.')