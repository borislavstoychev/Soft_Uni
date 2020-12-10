bad_rating = int(input())
last_examp =''
num_examp = 0
r = 0
b_r = 0
intp = input()
has_pass = True
while intp != 'Enough':
    name_examp = intp
    rating = float(input())
    r += rating
    num_examp += 1
    last_examp = name_examp

    if rating <= 4:
        b_r += 1
        if b_r == bad_rating:
            has_pass = False
            break
    intp = input()

if has_pass == False:
    print(f'You need a break, {b_r} poor grades.')
else:
    print(f'Average score: {r / num_examp:.2f}')
    print(f'Number of problems: {num_examp}')
    print(f'Last problem: {last_examp}')

