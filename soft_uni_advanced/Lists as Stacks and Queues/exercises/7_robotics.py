from datetime import datetime, timedelta
from collections import deque

available_robots = deque(input().split(";"))
start_time = datetime.strptime(input(), "%H:%M:%S")
working_robots = deque()
robots_dict = {}
products = deque()
product = input()
time = 0
while not product == "End":
    products.append(product)
    product = input()
while products:
    for current_robot in working_robots:
        current_robot[1] -= 1
        name = current_robot[0]
        if current_robot[1] <= 0:
            available_robots.append(f"{name}-{robots_dict[name]}")
    working_robots = [r for r in working_robots if r[1] > 0]

    time += 1
    element = products.popleft()
    if not available_robots:
        products.append(element)
        continue
    robots = available_robots.popleft()
    robot, product_time = robots.split("-")
    robots_dict[robot] = product_time
    working_robots.append([robot, int(product_time)])
    time_after_start = (start_time + timedelta(seconds=time))\
        .strftime("%H:%M:%S")
    print(f"{robot} - {element} [{time_after_start}]")
