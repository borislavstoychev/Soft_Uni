name_of_product = input()
city = input()
qty = float(input())
if city == "Sofia":
    if name_of_product == 'coffee':
        print(qty * 0.50)
    elif name_of_product == 'water':
        print(qty * 0.80)
    elif name_of_product == 'beer':
        print(qty * 1.20)
    elif name_of_product == 'sweets':
        print(qty * 1.45)
    elif name_of_product == 'peanuts':
        print(qty * 1.60)
elif city == 'Plovdiv':
    if name_of_product == 'coffee':
        print(qty * 0.40)
    elif name_of_product == 'water':
        print(qty * 0.70)
    elif name_of_product == 'beer':
        print(qty * 1.15)
    elif name_of_product == 'sweets':
        print(qty * 1.30)
    elif name_of_product == 'peanuts':
        print(qty * 1.50)
elif city == 'Varna':
    if name_of_product == 'coffee':
        print(qty *0.45)
    elif name_of_product == 'water':
        print(qty * 0.70)
    elif name_of_product == 'beer':
        print(qty * 1.10)
    elif name_of_product == 'sweets':
        print(qty * 1.35)
    elif name_of_product == 'peanuts':
        print(qty * 1.55)