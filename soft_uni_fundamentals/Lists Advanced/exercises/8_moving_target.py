targets = list(map(int, input().split()))


def shoot_target(nums, i, v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums


def add_target(nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print("Invalid placement!")
    return nums


def strike_target(nums, i, v):
    left_index = i - v
    right_index = i + v
    if left_index >= 0 and right_index < len(nums):
        left_part = nums[:left_index]
        right_part = nums[right_index + 1:]
        nums = left_part + right_part
    else:
        print("Strike missed!")
    return nums


commands = input()
while not commands == "End":
    command, index, target = commands.split()
    index = int(index)
    target = int(target)
    if command == "Shoot":
        targets = shoot_target(targets, index, target)
    elif command == "Add":
        targets = add_target(targets, index, target)
    elif command == "Strike":
        targets = strike_target(targets, index, target)

    commands = input()


print("|".join(map(str, targets)))
