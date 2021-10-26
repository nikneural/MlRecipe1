# Требуется преобразовать матрицу в одномерный массив

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.flatten())

# или метод reshape

print(matrix.reshape(1, -1))