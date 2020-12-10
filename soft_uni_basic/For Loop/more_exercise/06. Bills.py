n_months = int(input())
water = 0
internet = 0
electricity = 0
others = 0
av = 0
p1, p2, p3 = (0, 0, 0)
for i in range(1, n_months + 1):
    electricity = float(input())
    p1 += electricity
    water = 20
    p2 += water
    internet = 15
    p3 += internet
    others += (electricity + water + internet) * 0.2 + (electricity + water + internet)
av = (p1 + p2 + p3 + others) / n_months
print(f'Electricity: {p1:.2f} lv')
print(f'Water: {p2:.2f} lv')
print(f'Internet: {p3:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {av:.2f} lv')