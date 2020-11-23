list_of_integer = input().split()
n_removed = int(input())

list_of_num = []

for list_of_integer in list_of_integer:
    list_of_num.append(int(list_of_integer))

for removed in range(n_removed):
    list_of_num.remove(min(list_of_num))
print(list_of_num)
