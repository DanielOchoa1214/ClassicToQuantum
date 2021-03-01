import numpy as np


# Este modulo es de funciones de apoyo para el modulo principal el cual es deterministicSystems.py


def npToList(vector):
    transposed_vector = np.array([])
    for i in range(len(vector)):
        for j in range(0, 2):
            if j == 0:
                transposed_vector = np.append(transposed_vector, vector[i][j])
    return transposed_vector


def isUnitary(matrix):
    ad_matrix = matrix.transpose().conjugate()
    if np.array_equal(np.dot(matrix, ad_matrix), np.identity(len(matrix))):
        return True
    return False
