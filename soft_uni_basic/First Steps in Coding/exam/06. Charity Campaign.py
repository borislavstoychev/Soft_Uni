numbers_of_days = int(input())
numbers_of_cookers = int(input())
numbers_of_cake = int(input()) * 45
numbers_of_waffles = int(input()) * 5.80
numbers_of_pancakes = int(input()) * 3.20
result = numbers_of_cookers * numbers_of_days * (numbers_of_cake + numbers_of_waffles  + numbers_of_pancakes)
finale_result = result - result * 1 / 8
print(finale_result)
