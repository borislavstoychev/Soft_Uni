kind_of_cat = input()
sex = input()

if kind_of_cat == 'British Shorthair':
    if sex == 'm':
        years_of_life = (13 * 12) / 6
    elif sex == 'f':
        years_of_life = (14 * 12) / 6
    print(f'{round(years_of_life)} cat months')
elif kind_of_cat == 'Siamese':
    if sex == 'm':
        years_of_life = (15 * 12) / 6
    elif sex == 'f':
        years_of_life = (16 * 12) / 6
    print(f'{round(years_of_life)} cat months')
elif kind_of_cat == 'Persian':
    if sex == 'm':
        years_of_life = (14 * 12) / 6
    elif sex == 'f':
        years_of_life = (15 * 12) / 6
    print(f'{round(years_of_life)} cat months')
elif kind_of_cat == 'Ragdoll':
    if sex == 'm':
        years_of_life = (16 * 12) / 6
    elif sex == 'f':
        years_of_life = (17 * 12) /6
    print(f'{round(years_of_life)} cat months')
elif kind_of_cat == 'American Shorthair':
    if sex == 'm':
        years_of_life = (12 * 12) / 6
    elif sex == 'f':
        years_of_life = (13 * 12) / 6
    print(f'{round(years_of_life)} cat months')
elif kind_of_cat == 'Siberian':
    if sex == 'm':
        years_of_life = (11 * 12) / 6
    elif sex == 'f':
        years_of_life = (12 * 12) / 6
    print(f'{round(years_of_life)} cat months')
else:
    print(f'{kind_of_cat} is invalid cat!')