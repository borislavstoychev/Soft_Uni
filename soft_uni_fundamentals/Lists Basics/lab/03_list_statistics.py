n = int(input())
list_positive = []
list_negative = []
count_negative = 0
count_positive = 0
for i in range(n):
    num = int(input())
    if num < 0:
        list_negative.append(num)
        count_negative += num
    elif num > 0:
        list_positive.append(num)
        count_positive += 1
print(list_positive)
print(list_negative)
print(f'Count of positives: {count_positive}. Sum of negatives: {count_negative}')