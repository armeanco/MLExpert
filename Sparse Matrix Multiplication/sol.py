def sparse_matrix_multiplication(matrix_a, matrix_b):
    sparse = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    if len(matrix_a[0]) != len(matrix_b) and len(matrix_a) != len(matrix_b[0]):
        return [[]]
    for x in range(0, len(matrix_a)):
        for y in range(0, len(matrix_b[0])):
            dot_product = 0
            for i in range(0, len(matrix_a[0])):
                dot_product += matrix_a[x][i] * matrix_b[i][y]
            sparse[x][y] = dot_product
    return sparse
