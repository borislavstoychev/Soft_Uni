matrix = [[int(r) for r in input().split(", ")]for _ in range(int(input()))]
first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[j][len(matrix) - 1 - j] for j in range(len(matrix))]
print(f"First diagonal: {', '.join(list(map(str, first_diagonal)))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(list(map(str, second_diagonal)))}. Sum: {sum(second_diagonal)}")
