rows, columns = list(map(int, input().split(", ")))
matrix = []
total = 0
for i in range(rows):
    matrix.append(list(map(int, (input().split(", ")))))
    total += sum(matrix[i])
print(total)
print(matrix)

