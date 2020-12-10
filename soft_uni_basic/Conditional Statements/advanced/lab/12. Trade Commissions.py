town = input()
sales = float(input())
if town == "Sofia":
    if sales >= 0 and sales <= 500:
        comission = 0.05
    elif sales > 500 and sales <= 1000:
        comission = 0.07
    elif sales > 1000 and sales <= 10000:
        comission = 0.08
    elif sales > 10000:
        comission = 0.12
    else:
        comission = 0
elif town == "Varna":
    if sales >= 0 and sales <= 500:
        comission = 0.045
    elif sales > 500 and sales <= 1000:
        comission = 0.075
    elif sales > 1000 and sales <= 10000:
        comission = 0.1
    elif sales > 10000:
        comission = 0.13
    else:
        comission = 0
elif town == "Plovdiv":
    if sales >= 0 and sales <= 500:
        comission = 0.055
    elif sales > 500 and sales <= 1000:
        comission = 0.08
    elif sales > 1000 and sales <= 10000:
        comission = 0.12
    elif sales > 10000:
        comission = 0.145
    else:
        comission = 0
elif town != 'Sofia' or town != 'Plovdiv' or town != 'Varna':
    comission = 0
if comission > 0:
        print(f"{sales * comission:.2f}")
else:
    print('error')