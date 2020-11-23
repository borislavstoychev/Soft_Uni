foods = input().split()
foods_dic = {}
for index in range(0, len(foods), 2):
    key = foods[index]
    value = foods[index + 1]
    foods_dic[key] = int(value)
check_foods = input().split()
for food in check_foods:
    if food in foods:
        print(f"We have {foods_dic[food]} of {food} left")
    else:
        print(f"Sorry, we don't have {food}")