single_string = input().split(', ')
num_of_beggars = int(input())


got_sums_beggars = []

for single_string in single_string:
    num = int(single_string)
    got_sums_beggars.append(num)
beggar = []
for i in range(num_of_beggars):
    beggar.append(0)
index = 0
for num in got_sums_beggars:
    beggar[index] += num
    index += 1
    if index == num_of_beggars:
        index = 0

print(beggar)