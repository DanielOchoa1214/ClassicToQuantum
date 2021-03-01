import numpy as np
import matplotlib.pyplot as plt
from suportFunctions import *
import math


def dynamicStates(matrix_dynamics, state, clicks):
    movement = np.linalg.matrix_power(matrix_dynamics, clicks)
    return np.dot(movement, state)


def probabilisticSlits(slits, divisions, targets):
    first_probable_path = 1/slits
    matrix_dynamics = np.array([[0.0 for i in range(slits + targets + 1)]for j in range(slits + targets + 1)])
    for i in range(len(matrix_dynamics)):
        for j in range(len(matrix_dynamics)):
            if j == 0 and (0 < i <= slits):
                matrix_dynamics[i][j] = first_probable_path
            if i == j and j > slits:
                matrix_dynamics[i][j] = 1
    # Ya que no hay manera de saber con certeza que caminos puede cojer la bala cuando atravieza los huecos, se asume
    # que usuario ingresa los datos de que caminos puede cojer. En las lista divisions esta esta compuesta por listas
    # de 3 elementos donde el primero es el nodo de donde sale, el segundo a donde llega y el tercero la probabilidad de
    # que la bala vaya por esa direccion.
    for i in divisions:
        matrix_dynamics[i[1]][i[0]] = i[2]
    initial_state = np.array([[0] for i in range(len(matrix_dynamics))])
    initial_state[0] = [1]
    return dynamicStates(matrix_dynamics, initial_state, 2)


def quantumSlits(slits, divisions, targets):
    # las primera divisiones ahora seran la raiz del inverso de los posibles caminos para que se cumpla que |c|^2 = 1/slits
    first_probable_path = math.sqrt(1/slits)
    matrix_dynamics = np.array([[0 + 0j for i in range(slits + targets + 1)]for j in range(slits + targets + 1)])
    for i in range(len(matrix_dynamics)):
        for j in range(len(matrix_dynamics)):
            if j == 0 and (0 < i <= slits):
                matrix_dynamics[i][j] = first_probable_path
            if i == j and j > slits:
                matrix_dynamics[i][j] = 1
    for i in divisions:
        matrix_dynamics[i[1]][i[0]] = i[2]
    initial_state = np.array([[0] for i in range(len(matrix_dynamics))])
    initial_state[0] = [1]
    return dynamicStates(matrix_dynamics, initial_state, 2)


def printImage(state):
    objects = [f'Node {i}' for i in range(len(state))]
    y_pos = np.arange(len(objects))
    performance = npToList(state)

    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects)
    plt.ylabel('Probability')
    plt.title('Distribution after k clicks')

    plt.show()


slits = 2
divisions = [[1, 3, 1/np.sqrt(3)], [1, 4, 1/np.sqrt(3)],
                     [1, 5, 1/np.sqrt(3)], [2, 5, -1/np.sqrt(3)],
                     [2, 6, 1/np.sqrt(3)], [2, 7, 1/np.sqrt(3)]]
targets = 5
print(quantumSlits(slits, divisions, targets))