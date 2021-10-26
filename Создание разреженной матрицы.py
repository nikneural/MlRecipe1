# Имеются данные с очень малым количеством ненулевых значений,
# которые требуется эффективно представить

import numpy as np
from scipy import sparse

matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

# Создать сжатую разреженную матрицу-строку
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)