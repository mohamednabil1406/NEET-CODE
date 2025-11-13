def rotate(matrix):
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for i in range(n):
        matrix[i].reverse()

matrix = [
  [1,2],
  [3,4]
]

rotate(matrix)
print(matrix)
