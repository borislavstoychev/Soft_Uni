from  math import floor
biscuits_per_worker = int(input())
workers = int(input())
competing_factory = int(input())
biscuits = 0
for days in range(1, 31):
    biscuits_per_day = workers * biscuits_per_worker
    if days % 3 == 0:
        biscuits += floor(biscuits_per_day * 0.75)
    else:
        biscuits += biscuits_per_day
print(f"You have produced {biscuits} biscuits for the past month.")
diff = biscuits - competing_factory
percent = abs(diff) / competing_factory * 100
if diff > 0:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    print(f"You produce {percent:.2f} percent less biscuits.")