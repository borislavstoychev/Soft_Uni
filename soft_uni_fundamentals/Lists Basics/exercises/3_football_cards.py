# a = 11
# b = 11
#
# is_finish = False
#
# line = input()
#
# line_list = line.split()
#
#
# count_A = []
# count_B = []
# for i in line_list:
#     if 'A' in i:
#         count_A.append(i)
#     if 'B' in i:
#         count_B.append(i)
# for A in set(count_A):
#     a -= 1
#     if a < 7:
#         is_finish = True
#         break
# for B in set(count_B):
#     b -= 1
#     if b < 7:
#         is_finish = True
#         break
#
# print(f'Team A - {a}; Team B - {b}')
# if is_finish:
#     print('Game was terminated')

a = 11
b = 11

line = input()
line_list = line.split()
finale_list = set(line_list)
line2 = ''.join(finale_list)
this_list = list(line2)

A = this_list.count('A')
B = this_list.count('B')

if A > 4:
    A = 5
    print(f'Team A - {a - A}; Team B - {b - B}')
    print('Game was terminated')
elif B > 4:
    B = 5
    print(f'Team A - {a - A}; Team B - {b - B}')
    print('Game was terminated')
else:
    print(f'Team A - {a - A}; Team B - {b - B}')