money_needed = float(input())
months = int(input())
money_save = 0
for month in range(1, months + 1):
    if not month % 2 == 0 and month > 1:
        money_save -= money_save * 0.16
    if month % 4 == 0:
        money_save += money_save * 0.25
    money_save += money_needed * 0.25
if money_save - money_needed >= 0:
    print(f"Bravo! You can go to Disneyland and you will have {money_save - money_needed:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {money_needed - money_save:.2f}lv. more.")

