matrix = [list(map(int, (input().split()))) for i in range(int(input()))]
print(sum(matrix[i][i] for i in range(len(matrix))))