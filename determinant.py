import matrix as mt
import gaussian_eliminate as ge

def determinant(A):
    # Kiểm tra ma trận vuông
    n = len(A)
    m = len(A[0])
    if n != m:
        raise ValueError("Chỉ có thể tính định thức cho ma trận vuông.")

    # Gọi hàm khử Gauss. Truyền None cho vector b
    newMatrix, _, swaps = ge.gaussian_eliminate(A, None)

    # Tính tích các phần tử trên đường chéo chính
    det = 1.0
    for i in range(n):
        det *= newMatrix[i][i]

    # Đổi dấu định thức nếu số lần hoán đổi hàng là số lẻ
    if swaps % 2 != 0:
        det = -det

    return det

def main():
    # Khởi tạo ma trận bằng class mt.Matrix
    # Sử dụng phần ma trận A (3x3), vector b có thể giữ nguyên không ảnh hưởng
    matrixA = mt.Matrix(((1, 2, 3), 
                         (2, 3, 3), 
                         (3, 1, 4)), 
                         (2, 4, 7))

    print("--- Ma trận A ban đầu ---")
    for r in matrixA.A: 
        print(r)
    
    # Gọi hàm tính định thức và truyền vào phần tử A của class Matrix
    det = determinant(matrixA.A)

    print(f"\n=> Định thức của ma trận (det A) = {det}")

if __name__ == "__main__":
    main()