foods = input().split()
foods_dic = {}
for index in range(0, len(foods), 2):
    key = foods[index]
    value = foods[index + 1]
    foods_dic[key] = int(value)
print(foods_dic)

