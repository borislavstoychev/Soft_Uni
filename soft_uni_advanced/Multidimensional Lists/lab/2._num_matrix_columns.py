rows, columns = list(map(int, input().split(", ")))
matrix = [list(map(int, (input().split()))) for i in range(rows)]
for col in zip(*matrix):
    print(sum(col))
