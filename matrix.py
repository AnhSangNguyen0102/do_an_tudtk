class Matrix:
    Zero = 1e-10
    def __init__(self, matrix, b=None):
        self.A = [list(map(float, row)) for row in matrix]
        self.n = len(self.A)
        self.m = len(self.A[0])
        self.b = [float(x) for x in b] if b is not None else None

    @staticmethod
    def swapRows(mat, i, j):
        mat[i], mat[j] = mat[j], mat[i]

    @staticmethod
    def copyMatrix(mat):
        return [row[:] for row in mat]

    @staticmethod
    def display(self, mat, title="Ma trận"):
        for row in mat:
            print([round(x, 4) for x in row])
                     
            