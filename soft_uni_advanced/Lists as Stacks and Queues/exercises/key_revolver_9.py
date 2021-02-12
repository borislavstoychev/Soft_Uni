from collections import deque

bullet = int(input())
gun_barrel = int(input())
bullets = deque(int(n) for n in input().split())
locks = deque(int(num) for num in input().split())
intelligence = int(input())
shooting = 0
while bullets and locks:
    bullet_shoot = bullets.pop()
    lock = locks.popleft()
    shooting += 1
    if bullet_shoot > lock:
        locks.appendleft(lock)
        print("Ping!")
    else:
        print("Bang!")
    if shooting % gun_barrel == 0 and bullets:
        print("Reloading!")
bullet_cost = shooting * bullet
earned = intelligence - bullet_cost
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned}")