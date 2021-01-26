rows, columns = list(map(int, input().split()))
matrix = [[f"{chr(num)}{chr(n)}{chr(num)}" for n in range(num, num + columns)] for num in range(97, 97 + rows)]
[print(*m)for m in matrix]
