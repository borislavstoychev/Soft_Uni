matrix = [[int(el) for el in input().split(", ")] for _ in range(int(input()))]
print([val for sublist in matrix for val in sublist])
