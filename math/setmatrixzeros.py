def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zero = False
    first_col_zero = False

    # Step 1: Check first row
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True

    # Step 1: Check first column
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True

    # Step 2: Mark rows and columns
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 3: Fill cells based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 4: Fix first row
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Step 4: Fix first column
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
