steps_needed = 10000

steps_counter = 0
steps_home = 0
while steps_counter < steps_needed:
    command = input()
    if command == 'Going home':
        steps_home = int(input())
        steps_counter += steps_home
        if steps_counter < steps_needed:
            print(f'{steps_needed - steps_counter} more steps to reach goal.')
        break
    steps = int(command)
    steps_counter += steps
    if steps_counter >= steps_needed:
        break
if steps_counter >= steps_needed:
    print('Goal reached! Good job!')
    print(f'{steps_counter - steps_needed} steps over the goal!')
