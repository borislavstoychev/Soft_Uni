test_str = input()
upper = ''
this_list = []
for i in range(len(test_str)):
    if test_str[i].isupper():
        upper = i
        this_list.append(upper)
print(this_list)



