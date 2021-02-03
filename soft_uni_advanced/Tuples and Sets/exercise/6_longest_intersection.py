intersections = []
for n in range(int(input())):
    first_set = set()
    second_set = set()
    first_range, second_range = input().split("-")
    n1, n2 = first_range.split(",")
    n3, n4 = second_range.split(",")
    for f1 in range(int(n1), int(n2) + 1):
        first_set.add(f1)
    for f2 in range(int(n3), int(n4) + 1):
        second_set.add(f2)
    intersections.append(first_set & second_set)
max_intersection = (list(max(intersections, key=lambda x: len(x))))
print(f"Longest intersection is {max_intersection} with length {len(max_intersection)}")
