HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)

types_of_fairs = input().split("#")

amount_of_water = int(input())

efforts = 0
total_fair = 0
fair_list = []

for fairs in types_of_fairs:
    type_of_fair, size = fairs.split(" = ")
    fair = int(size)
    if type_of_fair == "High" and fair not in HIGH_RANGE:
        continue
    elif type_of_fair == "Medium" and fair not in MEDIUM_RANGE:
        continue
    elif type_of_fair == "Low" and fair not in LOW_RANGE:
        continue
    if amount_of_water >= fair:
        efforts += fair * 0.25
        total_fair += fair
        amount_of_water -= fair
        fair_list.append(fair)

print("Cells:")

for kill_fair in fair_list:
    print(f' - {kill_fair}')
print(f"Effort: {efforts:.2f}")
print(f"Total Fire: {total_fair}")



