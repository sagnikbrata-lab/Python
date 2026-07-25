def multiply_matrices(matrix_A, matrix_B):

    # Getting dimensions
    n = len(matrix_A)
    m = len(matrix_A[0])
    p = len(matrix_B)
    q = len(matrix_B[0])

    # Checking possibility of multiplication
    if m != p:
        return None

    # Creating an nxq result matrix padded with cyphers
    result = [[0 for _ in range(q)] for _ in range(n)]

    # Performing multiplication through 3 nested loops
    for i in range(n):
        for j in range(q):
            for k in range(m):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result

# Example 

# Matrix A is 4x3 (n = 4, m = 3)
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# Matrix B is 3x2 (p = 3, q = 2)
B = [
    [13, 14],
    [15, 16],
    [17, 18]
]

# Matrix C is 3x3 (n1 = 3, m1 = 3)
C = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]

# Here we go!
P = multiply_matrices(A, B)
Q = multiply_matrices(B, C)
R = multiply_matrices(A, C)
S = multiply_matrices(C, A)

results = [
    ("A x B", P),
    ("B x C", Q),
    ("A x C", R),
    ("C x A", S)
]

# Display result 
for name, matrix in results:
    print(name)
    if matrix is not None:
        print("Resulting Matrix is: ")
        for row in matrix:
            print(row)
    else:
        print("Matrix multiplication is not possible!")





    