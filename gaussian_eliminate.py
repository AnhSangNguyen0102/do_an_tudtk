import matrix as mt

def gaussian_eliminate(A, b):
    newMatrix = mt.Matrix.copyMatrix(A)
    n = len(A)
    m = len(A[0])
    b_new = b[:] if b else None
    swaps = 0
    row = 0
    for col in range(m):
        if row >= n: break
        maxRow = row
        for i in range(row + 1, n):
            if(abs(newMatrix[i][col]) > abs(newMatrix[maxRow][col])): 
                maxRow = i

        if abs(newMatrix[maxRow][col]) < mt.Matrix.Zero:
            continue

        if maxRow != row:
            mt.Matrix.swapRows(newMatrix, maxRow, row)
            if b_new is not None:
                b_new[row], b_new[maxRow] = b_new[maxRow], b_new[row]
            swaps += 1

        for i in range(row + 1, n):
            factor = newMatrix[i][col] / newMatrix[row][col]
            for j in range(col, m):
                newMatrix[i][j] -= factor * newMatrix[row][j]
            if b_new is not None:
                b_new[i] -= factor * b_new[row]
        row += 1

    return newMatrix, b_new, swaps

def main():
    matrixA = mt.Matrix(((1, 2, 3), (2, 3, 3), (3, 1, 4)), (2, 4, 7))

    newmatrix, b_new, swaps = gaussian_eliminate(matrixA.A, matrixA.b)

    print("--- Ma trận sau khi khử ---")
    for r in newmatrix: print(r)
    
    print(f"\nVector b mới: {b_new}")
    print(f"Số lần hoán đổi: {swaps}")

if __name__ == "__main__":
    main()