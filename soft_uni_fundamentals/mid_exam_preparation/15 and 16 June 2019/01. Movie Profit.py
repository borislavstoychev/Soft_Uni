name = input()
num_of_days = int(input())
tickets = int(input())
price_of_ticket = float(input())
percent_cinema = int(input())

price_per_day = tickets * price_of_ticket
price = num_of_days * price_per_day
price -= price * percent_cinema / 100
print(f'The profit from the movie {name} is {price:.2f} lv.')