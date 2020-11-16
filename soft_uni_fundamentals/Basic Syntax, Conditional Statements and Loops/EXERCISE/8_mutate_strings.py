str_1 = input()
str_2 = input()

list_1 = list(str_1)
list_2 = list(str_2)

for k in range(len(str_1)):
    if not list_1[k] == list_2[k]:
        list_1[k] = list_2[k]
        print(''.join(list_1))

# current_str = ''
# previews_str = str_1
# for iteration in range(len(str_1)):
#     for index_str_2 in range(iteration + 1):
#         current_str += str_2[index_str_2]
#     for index_str_1 in range(iteration + 1, len(str_1)):
#         current_str += str_1[index_str_1]
#     if not current_str == previews_str:
#         print(current_str)
#     previews_str = current_str
#     current_str = ''