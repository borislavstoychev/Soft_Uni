movie = input()
pockets = input()
tickets = int(input())
if pockets == "Drink":
    if movie == 'John Wick':
        price = 12 * tickets
    elif movie == 'Star Wars':
        price = 18 * tickets
    elif movie == 'Jumanji':
        price = 9 * tickets
elif pockets == 'Popcorn':
    if movie == 'John Wick':
        price = 15 * tickets
    elif movie == 'Star Wars':
        price = 25 * tickets
    elif movie == 'Jumanji':
        price = 11 * tickets
elif pockets == 'Menu':
    if movie == 'John Wick':
        price = 19 * tickets
    elif movie == 'Star Wars':
        price = 30 * tickets
    elif movie == 'Jumanji':
        price = 14 * tickets
if tickets >= 4 and movie == 'Star Wars':
    price *= 0.7
if tickets == 2 and movie == 'Jumanji':
    price *= 0.85
print(f'Your bill is {price:.2f} leva.')