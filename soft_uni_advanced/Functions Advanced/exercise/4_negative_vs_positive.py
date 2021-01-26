def kind_of_numbers(nums):
    negative = []
    positive = []
    for n in nums:
        if n >= 0:
            positive.append(n)
        else:
            negative.append(abs(n))
    return negative, positive


negative_nums, positive_nums = kind_of_numbers([int(n) for n in input().split()])
negative_nums, positive_nums = sum(negative_nums), sum(positive_nums)
print(f"-{negative_nums}")
print(f"{positive_nums}")
if negative_nums > positive_nums:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")