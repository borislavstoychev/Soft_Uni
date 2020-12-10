type_of_projection = input()
num_of_rows = int(input())
num_of_columns = int(input())
income = 0
cinema_capacity = num_of_rows * num_of_columns
if type_of_projection == 'Premiere':
    income = cinema_capacity * 12
elif type_of_projection == 'Normal':
    income = cinema_capacity * 7.50
elif type_of_projection == 'Discount':
    income = cinema_capacity * 5
print(f'{income: .2f} leva')
