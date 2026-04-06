import numpy as np
from scipy.linalg import orth, null_space
import matrix as mt
import rank_and_basis as rab
import inverse as inv
import determinant as dtm
import back_substitution as bs
import gaussian_eliminate as ge


def verify_solution(A, x, b):    # Kiểm tra lại tính đúng đắn của các hàm bằng các hàm 
    newMatrix = np.array(A)      # có sẵn từ numpy
    if np.linalg.inv(A) != inv.inverse(newMatrix):
        print("Hàm nghịch đảo có lỗi!");
    else: 
        print("Hàm nghịch đảo đúng!")

    if np.linalg.det(A) != dtm.determinant(newMatrix):
        print("Hàm định thức có lỗi!");
    else: 
        print("Hàm định thức đúng!")

    if np.linalg.solve(A) != bs.back_substitution(newMatrix):
        print("Hàm giải hệ phương trình có lỗi!");
    else: 
        print("Hàm giải hệ phương trình đúng!")

    rank = np.linalg.matrix_rank(A)
    colBasis = orth(A)
    rowBasis = orth(A.T)
    nghiemBasis = null_space(A)
    hang, csCot, csDong, csNghiem = rab.rank_and_basis(A)

    if rank != hang:
        print("Hạng của ma trận sai!")
    elif colBasis != csCot:
        print("Vector cơ sở cột sai!")
    elif rowBasis != csDong:
        print("Vector cơ sở dòng sai!")
    elif nghiemBasis != csNghiem:
        print("Vector cơ sở nghiệm sai!")
    else:
        print("Hàm tính hạng và cơ sở đúng")

