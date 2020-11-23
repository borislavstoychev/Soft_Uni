factor = int(input())
count = int(input())
long = factor * count
this_list = []
for i in range(factor, long + factor, factor):
    this_list.append(i)

print(this_list)
