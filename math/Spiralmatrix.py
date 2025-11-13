def spiral(matrix):
    res = []
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    step = [len(matrix[0]), len(matrix) - 1]

    r, c, d = 0, -1, 0

    while step[d & 1]:
        for _ in range(step[d & 1]):
            r += directions[d][0]
            c += directions[d][1]
            res.append(matrix[r][c])

        step[d & 1] -= 1
        d = (d + 1) % 4

    return res


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(spiral(matrix))
