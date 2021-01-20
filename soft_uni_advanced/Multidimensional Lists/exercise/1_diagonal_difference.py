matrix = [list(map(int, (input().split()))) for _ in range(int(input()))]
print(abs(sum(matrix[i][i] for i in range(len(matrix))) - sum(matrix[j][len(matrix) - 1 - j] for j in range(len(matrix)))))

