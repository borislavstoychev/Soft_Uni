from collections import deque

n = int(input())
orders = deque(list(map(int, input().split())))
max_order = max(orders)
while orders:
    order = orders.popleft()
    if order > n:
        orders.appendleft(order)
        break
    n -= order
print(f"{max_order}")
if orders:
    print(f"Orders left:", end=" ")
    print(*orders)
else:
    print("Orders complete")


